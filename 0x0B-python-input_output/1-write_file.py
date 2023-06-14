#!/usr/bin/python3
"""This file contains a function that reads a text file"""


def write_file(filename="", text=""):
    """This function reads a text file and returns
    the read file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f = f.write(text)
        return f
