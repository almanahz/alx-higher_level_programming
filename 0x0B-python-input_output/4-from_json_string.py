#!/usr/bin/python3
from json import loads
"""This file contains a function that performs some
JSON opertion"""


def from_json_string(my_str):
    """desc: This function performs some JSON operation
    return: object represented by JSON string"""
    return loads(my_str)
