#!/usr/bin/python3
from models.base_model import BaseModel
"""user model"""

class User(BaseModel):
    """ Class user that inherits from base_model """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
