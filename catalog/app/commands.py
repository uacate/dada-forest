# https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/

import json
import os
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# from datetime import datetime
import requests

# from psycopg2.errors import UniqueViolation
from models import Document, Base

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
db_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@catalog_pgdb:5432"
engine = create_engine(db_url)


def init_db():
    Base.metadata.create_all(engine)


def load_data():
    with open("url_sources.json", "r") as f:
        data = json.load(f)
        documents = []
        for item in data:
            if item:
                url = item["url"]
                req = requests.get(url).json()
                if req:
                    identifier = req["identifier"]
                    description = req["description"]
                    document = Document(
                        identifier=identifier, url=url, description=description
                    )
                    documents.append(document)

        if documents and len(documents):
            with Session(engine) as session:
                session.add_all(documents)
                try:
                    session.commit()
                except IntegrityError as e:
                    # TODO: Need to add some logging here.
                    print(e)


if __name__ == "__main__":
    init_db()
    load_data()
