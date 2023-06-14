#!/usr/bin/python3
from json import dumps
"""This file contains a function that performs some
JSON opertion"""


def to_json_string(my_obj):
    """desc: This function performs some JSON operation
    return: JSON representation of an string"""
    return dumps(my_obj)
