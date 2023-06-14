#!/usr/bin/python3
"""This file contains a function that reads a text file"""


def read_file(filename=""):
    """This function reads a text file and returns
    the read file"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")

