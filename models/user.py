#!/usr/bin/python3

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
