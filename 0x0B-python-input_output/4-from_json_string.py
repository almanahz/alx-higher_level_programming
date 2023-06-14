#!/usr/bin/python3
"""This file contains a function that appends to a text file"""
import json


def from_json_string(my_str):
    """desc: This function performs some JSON operation
    return: object represented by JSON string"""
    return json.loads(my_str)
