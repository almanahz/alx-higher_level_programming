#!/usr/bin/python3
"""This file contains a class that
performs some operation on student information"""


class Student:
    """Receive students name as argument and set the JSON value"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
