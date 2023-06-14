#!/usr/bin/python3
"""This file contains a function that performs some
JSON opertion"""

from json import dump


def save_to_json_file(my_obj, filename):
    """desc: This function performs some JSON operation
    return: none"""
    with open(filename, mode='w', encoding='utf-8') as f:
        json_format = dump(my_obj)
        f.write(json_format)
