#!/usr/bin/python3
"""This file contains a function that inherit from a class"""


class MyLliist(list):
    """This class uses inherited method to perform some
    operations on a list"""

    def print_sorted(self):
        """This mwthod prints a sorted version of the instance"""
        print(sorted(self))
