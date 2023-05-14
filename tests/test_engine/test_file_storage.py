#!/usr/bin/python
"""test_file_storage module"""
import sys
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestFileStorage:
    """test class for file_storage module"""

    def setUp(self):
        """setting up"""
        self.module = FileStorage()

    def tearDown(self):
        """clean up"""
        self.module = None

    def test_FileStorage_attr(self):
        """testing the type of FileStorage attribute"""
        self.assertEqual(self.model.__file_path, "file_path")
