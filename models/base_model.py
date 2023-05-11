#!/usr/bin/python3
"""This is the base model"""

import uuid
import datetime


class BaseModel():
    """This class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Creates a BaseModel instance"""

        if kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

        for key, value in kwargs.items():
            if key in ['created_at', 'updated_at']:
                self.__dict__[key] = datetime.fromisoformat(value)
            elif key != '__class__':
                self.__dict__[key] = value

    def __str__(self) -> str:
        """Returns the string representation of object"""
        class_name = self.__class__.__name__
        return f'[{class_name}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates updated_at with the current time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/valus of __dict__"""
        Base_dict = self.__dict__.copy()
        Base_dict['created_at'] = self.created_at.isoformat()
        Base_dict['updateded_at'] = self.updated_at.isoformat()
        Base_dict['__class__'] = self.__class__.__name__
        return Base_dict
