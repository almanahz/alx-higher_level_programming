#!/usr/bin/python3
"""This file contains a function that performs some
JSON opertion"""


from json import dumps
def to_json_string(my_obj):
    """desc: This function performs some JSON operation
    return: JSON representation of an string"""
    return dumps(my_obj)
