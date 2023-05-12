#!/usr/bin/python3
""" This module creates the review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ This classs inherits from Base Class and manages the review class """
    place_id = ""
    user_id = ""
    text = ""
