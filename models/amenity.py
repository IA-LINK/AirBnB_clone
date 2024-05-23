#!/usr/bin/python3
"""
Defines a module for the Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity is a class that inherit from a BaseModel.
    Defines amenities that users can choose from in places.
    Attribute:
        name <str> : name of the amenity
    """ 
    name = ""
    