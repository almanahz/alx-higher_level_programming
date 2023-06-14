#!/usr/bin/python3
"""This file contains a function that performs some JSON opertion"""
import json


def from_json_string(my_str):
    """desc: This function performs some JSON operation
    return: JSON representation of an string"""
    return json.dumps(my_str)
