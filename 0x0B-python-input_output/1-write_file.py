#!/usr/bin/python3
"""This file contains a function that writes
a string to a text file"""


def write_file(filename="", text=""):
    """desc: function writes a string to a text file
    return: number fo characters written"""
    with open(filename, mode='w', encoding='utf-8'):
        f.write(text)
