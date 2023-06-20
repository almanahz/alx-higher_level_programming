"""A module containing test cases for base class"""

import unittest
from models.base import Base
import sys


class TestBaseInstantiation(unittest.TestCase):
    """A class that tests various testcases for class Base"""
    
    def no_argument(self):
        """
        Test for initialization for class variable when no
        argument is passed
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id-1)
        self.assertEqual(b1.id, b3.id-2)

    def with_single_argument(self):
        """
        Test for initialization of class variable when an
        argument of various type  is passed
        """
        b1 = Base(0)
        b2 = Base("string")
        b3 = Base(-14)
        b4 = Base(12.45)
        b5 = Base([12, 145])
        
        self.assertEqual(b1.id, 0)
        self.assertEqual(b2.id, "string")
        self.assertEqual(b3.id, -14)
        self.assertEqual(b4.id, 12.45)
        self.assertEqual(b5.id, [12, 145])


