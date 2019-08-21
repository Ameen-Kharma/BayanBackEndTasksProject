from django.db import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, TIMESTAMP, func


class BaseModel(object):
    id = Column('id', Integer, primary_key=True, nullable=False)
    created = Column(TIMESTAMP, default=func.now())
    updated = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())


BayanBaseModel = declarative_base(cls=BaseModel)
