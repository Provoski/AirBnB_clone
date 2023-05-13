#!/usr/bin/python3
from models.base_model import BaseModel
""" review model"""


class Review(BaseModel):
    """ Class Review that inherits from base model """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
