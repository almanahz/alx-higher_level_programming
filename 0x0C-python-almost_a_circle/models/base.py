#!/usr/bin/python3
"""This file contains a class Base"""


class Base():
    """desc: assigns arg id to an object
    arg: id which is an integer"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
