from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import declarative_base

Base = declarative_base()
target_metadata = Base.metadata


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    identifier = Column(String(125), nullable=True, unique=True)
    url = Column(String(250), unique=False, nullable=True)
    description = Column(String(2500), unique=False, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
