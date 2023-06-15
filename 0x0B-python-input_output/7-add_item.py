#!/usr/bin/python3
"""This file contains a function that performs some
JSON opertion"""

from os import path
from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file
from sys import argv

if path.exists('add_item.json'):
    obj_json_file = load_from_json_file('add_item.json')
else:
    obj_json_file = []

for i in range(1, len(argv)):
    obj_json_file.append(argv[i])

save_to_json_file(obj_json_file, 'add_item.json')
