#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel



class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    
    email = ''
    password = ''
    first_name = None
    last_name = None

    def __init__(self, *args, **kwargs):
        """Initializes User instance"""
        super().__init__(*args, **kwargs)
