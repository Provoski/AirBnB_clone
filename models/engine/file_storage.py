#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
"""file_storage module"""


class FileStorage():
    """
    attributes: __file_path, __objects
    methods: all(), save()
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary:  __objects """
        return self.__objects

    def new(self, obj):
        """
        creates new object, where id is <class>.<id>
        """
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        save __objects dictionary to a jason file
        """
        objects = self.__objects
        obj_dict = {obj: objects[obj].to_dict() for obj in objects.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                for key, value in json.load(f).items():
                    attri_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attri_value
        except FileNotFoundError:
            pass
