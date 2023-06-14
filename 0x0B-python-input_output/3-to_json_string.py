#!/usr/bin/python3
from json import dumps
"""This file contains a function that performs some
JSON opertion"""


def from_json_string(my_str):
    """desc: This function performs some JSON operation
    return: JSON representation of an string"""
    return dumps(my_str)
