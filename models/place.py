#!/usr/bin/env python3
"""
This script containing the definition of Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    To defines the class Place with the following list of
    class attributes:
    city_id, user_id, name, description, number_rooms,
    number_bathrooms, max_guest, price_by_night,
    latitude, longitude, amenity_ids.
    """
    city_id = str()
    user_id = str()
    name = str()
    description = str()
    number_rooms = int()
    number_bathrooms = int()
    max_guest = int()
    price_by_night = int()
    latitude = float()
    longitude = float()
    amenity_ids = []
