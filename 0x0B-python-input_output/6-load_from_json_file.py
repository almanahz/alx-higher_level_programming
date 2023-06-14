#!/usr/bin/python3
from json import load
"""This file contains a function that performs some
JSON opertion"""

from json import loads


def load_from_json_file(filename):
    """desc: This function performs some JSON operation
    return: JSON object"""
    with open(filename, mode='r', encoding='utf-8') as f:
        return loads(f.read())
