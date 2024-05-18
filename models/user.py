#!/usr/bin/python3

<<<<<<< HEAD
from .base_model import BaseModel
"""This file is a User model that inherits from BaseModel"""

class User(BaseModel):
    """User lass User that inherits from BaseModel:"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
     
=======
"""
Defines a module for the User class
"""
from base_model import BaseModel

class User(BaseModel):
    """
    Represents an instance of a user
    """

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

    def __str__(self):
        return super().__str__()
>>>>>>> b5e85616077fbc29a1fbf2a2591464e6b01977f1
