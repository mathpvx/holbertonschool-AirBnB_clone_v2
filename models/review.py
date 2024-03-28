#!/usr/bin/python3
""" module for the HBNB project """
from sqlalchemy.sql.schema import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import String, Integer, Float

from models.base_model import BaseModel, Base
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Review(BaseModel, Base):
        """ review class storing review information """

        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
else:
    class Review(BaseModel):
        """ Review class storing review information """
        place_id = ""
        user_id = ""
        text = ""
