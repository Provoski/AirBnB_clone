#!/usr/bin/python3
from models.engine.file_storage import FileStorage
"""__init__ module"""

classes = {'BaseModel': 'BaseModel', 'Amenity': 'Amenity', 'State': 'State',
           'Place': 'Place', 'Review': 'Review', 'User': 'User'}
storage = FileStorage()
storage.reload()
