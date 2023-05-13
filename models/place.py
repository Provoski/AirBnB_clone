#!/usr/bin/python3
from models.base_model import BaseModel
"""place model"""


class Place(BaseModel):
    """ Class Place that inherits from base_model """

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

    def __init__(self, *args, **kwargs):
        """ Constructor """

        super().__init__(self, *args, **kwargs)
