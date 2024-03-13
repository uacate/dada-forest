import requests
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, crud

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def main():
    gila_nf_johnson_postfire_url = "https://catalog.data.gov/harvest/object/04643a90-e5fd-4602-a8fa-e8195dd16c5e"
    resp = requests.get(gila_nf_johnson_postfire_url)
    title = None
    descr = None
    # keyword = None
    if resp and resp.status_code == 200:
        resp_json = resp.json()
        if resp_json and len(resp_json) > 0:
            resp_keys = resp_json.keys()
            if "title" in resp_keys:
                title = resp_json["title"]
            if "description" in resp_keys:
                descr = resp_json["description"]
    #         # if "keyword" in resp_keys:
    #         #     keyword = resp_json["keyword"]

            entity = {
                "title": title,
                "description": descr,
                # "keywords": keyword
            }

            db = get_db()
            mde = crud.create_meta_data_entity(db, mde=entity)

    #         # mde = MetaDataEntity(**entity)
    #         # print(mde.model_dump())


if __name__ == "__main__":
    main()
