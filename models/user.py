#!/usr/bin/python3
""" This module creates a user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """ This class inherits from BaseModel and manages a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
