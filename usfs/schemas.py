from pydantic import BaseModel


class MetaDataEntity(BaseModel):
    title: str
    description: str
    # keywords: list

    class Config:
        model_validate = True
