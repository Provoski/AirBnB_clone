#!/usr/bin/python3
from models.base_model import BaseModel
"""city model"""


class City(BaseModel):
    """ Class State  that inherits from base_model """

    state_id = str()
    name = str()

    def __init__(self, *args, **kwargs):
        """ Constructor """

        super().__init__(self, *args, **kwargs)
