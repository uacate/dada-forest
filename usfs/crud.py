from sqlalchemy.orm import Session
import models, schemas


def create_meta_data_entity(db: Session, mde: schemas.MetaDataEntity):
    title = "Test Title"
    descr = "Test Description"
    mde = models.MetaDataEntity(title=title, description=descr)

    db.add(mde)
    db.refresh(mde)
    return mde

# def create_meta_data_entity(db: Session = Depends(get_db), entity: schemas.MetaDataEntity):
#     title = "Test Title"
#     descr = "Test Description"
    mde = models.MetaDataEntity(title=title, description=descr)
#     db.add(mde)
#     db.commit()
#     db.refresh(mde)
#     return mde