#!/usr/bin/python3

"""This file contains a class Base"""

from json import dumps, dump, loads


class Base:
    """desc: assigns arg id to an object
    arg: id which is an integer"""

    __nb_objects = 0

    def __init__(self, id=None):
        """It initializes the argument and variables"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A static method that returns JSON string representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A classmethod that writes JSON string to a file"""
        if list_objs is None:
            return []
        else:
            filename = f"{cls.__name__}.json"
            with open(filename, mode='w', encoding='utf-8') as f:
                to_write = [cls.to_dictionary() for cls in list_objs]
                dump(to_write, f)

    @staticmethod
    def from_json_string(json_string):
        """A staticmethods that returns the python representation
        of a JSON string"""
        if json_string is None or json_string == []:
            return []
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """A classmethod that returns an instance with
        all attributes already set"""
        dummy_instance = cls(1, 2)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """This method takes in no argument and returns
        the list of instances"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                list_dicts = Base.from_json_string(f.read())
                to_load = [cls.create(**dict) for dict in list_dicts]
                return to_load
        except IOError:
            return []
