#!/usr/bin/python3
"""This file performs some JSON operation"""


def class_to_json(obj):
    """it returns a dict"""
    return obj.__dict__
