#!/usr/bin/python3
"""
Defines a module for the Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel.
    Attributes:
        text (str): the review details of a place
        place_id (str): the id of the place a user is looking into
        user_id (str): the User id
    """
    place_id = ""  # It will be the Place.id
    user_id = ""  # It will be the User.id
    text = ""   # it will take text from user