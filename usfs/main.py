"""
https://github.com/tiangolo/sqlmodel/issues/85
https://catalog.data.gov/organization/usda-gov?_tags_limit=0&tags=usda-forest-service
https://catalog.data.gov/dataset?publisher=U.S.%20Forest%20Service
https://www.timescale.com/blog/postgresql-as-a-vector-database-create-store-and-query-openai-embeddings-with-pgvector/
https://thinhdanggroup.github.io/postgresql-vectordb/
"""
import psycopg2, requests, json
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from psycopg2.errors import UniqueViolation

load_dotenv()

def create_db_table():
    pgsql_url = "postgresql://postgres:sql77@localhost/postgres"
    host = "0.0.0.0"
    dbname = "postgres"
    user = "postgres"
    password = "sql77"

    sql = """
    -- public.document definition
    -- Drop table
    -- DROP TABLE public.document;
    CREATE TABLE IF NOT EXISTS public.document (
        id serial4 NOT NULL,
        identifier varchar NOT NULL,
        title varchar NOT NULL,
        description varchar NOT NULL,
        embedding public.vector NULL,
        CONSTRAINT document_identifier_key UNIQUE (identifier),
        CONSTRAINT document_pkey PRIMARY KEY (id)
    );
    """
    with psycopg2.connect(pgsql_url) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)

def get_meta_from_url(url):
    resp_json = None

    resp = requests.get(url)
    if resp and resp.status_code == 200:
        resp_json = resp.json()

    return resp_json

def save_meta_data(obj):
    pgsql_url = "postgresql://postgres:sql77@localhost/postgres"
    with psycopg2.connect(pgsql_url) as conn:
        with conn.cursor() as cursor:
            sql = "INSERT INTO document () "
            try:
                cursor.execute(sql)
            except UniqueViolation as e:
                pass

def save_documents(docs):

    sql = "INSERT INTO (document) VALUES ()"
    pgsql_url = "postgresql://postgres:sql77@localhost/postgres"
    with psycopg2.connect(pgsql_url) as conn:
        with conn.cursor() as cursor:
            for doc in docs:
                d = {"identifier": doc["identifier"], "title": doc["title"], "description": doc["description"], "embedding": doc["embedding"].tolist()}
                sql = """INSERT INTO document (identifier, title, description, embedding) VALUES (%(identifier)s, %(title)s, %(description)s, %(embedding)s)"""
                try:
                    cursor.execute(sql, d)
                except Exception as e:
                    pass

        conn.commit()

def query_docs(txt):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embedding = model.encode(txt).tolist()
    embeddings = ",".join(str(e) for e in embedding)
    embeddings = f"'[{embeddings}]'"
    sql = f"""SELECT id, title, description, 1 - (embedding <=> {embeddings}) AS cosine_similarity FROM document ORDER BY cosine_similarity DESC"""

    pgsql_url = "postgresql://postgres:sql77@localhost/postgres"
    with psycopg2.connect(pgsql_url) as conn:
        with conn.cursor() as cursor:#
            cursor.execute(sql, embedding)
            for row in cursor.fetchall():
                print(row)

def create_data():
    urls = [
        "https://catalog.data.gov/harvest/object/203bed83-5da3-4a64-b156-ea016f277b07",
        "https://catalog.data.gov/harvest/object/04643a90-e5fd-4602-a8fa-e8195dd16c5e",
        "https://catalog.data.gov/harvest/object/abf916ec-6ddd-4030-8f5e-3b317a33ba1e",
        "https://catalog.data.gov/harvest/object/589436ca-1324-4773-9201-acecd5d83448",
        "https://catalog.data.gov/harvest/object/21392fa4-ff86-4ac8-9f38-33d67aef770c",
        "https://catalog.data.gov/harvest/object/9216c0ce-d083-48a6-b017-e0efc0fada37",
        "https://catalog.data.gov/harvest/object/0b20b4e4-34f8-4d1d-ae1c-7a405d0f6d36",
        "https://catalog.data.gov/harvest/object/36b9144a-dc24-43cf-85c3-49a08dbed762",
        "https://catalog.data.gov/harvest/object/9d60be08-5c3b-45a7-8ae6-017a4ca9433c",
        "https://catalog.data.gov/harvest/object/a4a75240-4fac-40f7-a327-6596becff636",
        "https://catalog.data.gov/harvest/object/8df82322-0812-46c7-b2b3-52829a8417e1",
        "https://catalog.data.gov/harvest/object/0419db56-01a4-4a97-a4f0-1fb903e77cdf",
        "https://catalog.data.gov/harvest/object/32d5b113-e83c-48f3-b05a-fd99ed7a3a92",
        "https://catalog.data.gov/harvest/object/f2e66a1c-10b6-4243-920a-0b64352b8c63",
        "https://catalog.data.gov/harvest/object/a0a63e30-b3cb-418b-8616-d89ee2e9e100",
    ]

    docs = []
    descriptions = []
    model = SentenceTransformer("all-MiniLM-L6-v2")
    for url in urls:
        obj = get_meta_from_url(url)
        keys = obj.keys()
        title = ""
        descr = ""
        identifier = obj['identifier']
        if "title" in keys:
            title = obj["title"]
        if "description" in keys:
            descr = obj["description"].strip()

        docs.append({
            "identifier": identifier,
            "title": title,
            "description": descr,
            "embedding": None
        })

        descriptions.append(descr)

    description_embeddings = model.encode(descriptions)

    for index, doc in enumerate(docs):
        doc["embedding"] = description_embeddings[index]

    save_documents(docs)

def main():
    create_db_table()
    create_data()
    # query_docs("intensity")
    # query_docs("Best source of fire data")
    # query_docs("What is a good source of orthophotos?")
    # query_docs("watershed runoff")
    query_docs("Data about fish")

if __name__ == "__main__":
    main()
