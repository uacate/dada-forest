from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


class MetaDataEntity(Base):
    __tablename__ = "metadata_entity"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
