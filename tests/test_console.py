#!/usr/bin/python3
"""
    test_console module for the implementation of
    unittest for console module
"""
import sys
import unittest
import models
from io import StringIO
from unittest.mock import patch, mock_open, create_autospec
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """ test class for console nodule"""

    def setUp(self):
        """set up"""
        self.console = HBNBCommand()
        out = StringIO()
        sys.stdout = out

    def test_quit(self):
        """test for quit method"""
        self.assertTrue(hasattr(self.console, "do_quit"))

    def test_show(self):
        """test for show method"""
        self.assertTrue(hasattr(self.console, "do_show"))

    def test_all(self):
        """test for all method"""
        self.assertTrue(hasattr(self.console, "do_all"))

    def test_update(self):
        """test for update method"""
        self.assertTrue(hasattr(self.console, "do_update"))

    def test_destroy(self):
        """test for destroy method"""
        self.assertTrue(hasattr(self.console, "do_destroy"))

    def test_EOF(self):
        """test fro EOF"""
        self.assertTrue(hasattr(self.console, "do_EOF"))

    def tearDown(self):
        """clean up"""
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
