#!/usr/bin/python3
"""module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import DateTime
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer


from sqlalchemy.orm import relationship, backref
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class User(BaseModel, Base):
        """class defines a user by various attributes"""
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")
        reviews = relationship("Review", backref="user",
                               cascade="all, delete, delete-orphan")

else:
    class User(BaseModel):
        """class defines a user by various attributes"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
