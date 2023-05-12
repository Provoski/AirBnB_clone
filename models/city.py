#!/usr/bin/python3
""" This module creates a city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """ This classs inherits from Base Class and manages the city class"""
    state_id = ""
    name = ""
