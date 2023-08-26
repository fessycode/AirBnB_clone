#!/usr/bin/env python3
"""
This script containing the definition of Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines the class Amenity with the following list of
    class attributes:
    + `name`: string - empty string
    """
    name = str()
