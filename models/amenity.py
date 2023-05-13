#!/usr/bin/python3
from models.base_model import BaseModel
"""amenities model"""


class Amenity(BaseModel):
    """ Class Amenity that inherits from base_model """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
