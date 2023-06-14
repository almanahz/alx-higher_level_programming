#!/usr/bin/python3
"""This file contains a function that appends to a text file"""


def append_write(filename="", text=""):
    """desc: This function appends a text to a file
    return: number of characters added"""
    with open(filename, mode='a', encoding='utf-8') as f:
        f = f.write(text)
        return f
