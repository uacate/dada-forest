import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from models import Document, Base


load_dotenv()

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
db_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@catalog_pgdb:5432"
engine = create_engine(db_url)


def init_db():
    Base.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="DADA-Forest Catalog API", lifespan=lifespan)


@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <html>
        <head>
            <title>DADA-Forest</title>
        </head>
        <body>
            <div><a href="/docs">API Docs</a></div>
        </body>
    </html>
    """


@app.get("/health")
async def health():
    return {"data": "ok"}


@app.get("/simple-query/{term}")
async def simple_query(term: str) -> dict:
    """Simple search for a term or phrase.  Queries against the description field.

    Parameters:
    -----------
    term: str, required
        The search term or phrase.

    Returns:
    --------
    dict
        A dictionary
    """

    resp = []
    with Session(engine) as session:
        docs = (
            session.query(Document.identifier, Document.description)
            .filter(Document.description.ilike(f"%{term}%"))
            .all()
        )

        for d in docs:
            resp.append({"identifier": d[0], "description": d[1]})

    return {"message": term, "data": resp}
