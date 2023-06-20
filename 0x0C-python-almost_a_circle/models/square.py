#!/usr/bin/python3
"""This file contains class square that performs
some operation on the input"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """This serves as a constructor method that
        initializes all the variables"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """This method update an instance using non keyword argument
        and keyword argument"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[2]

        if not len(args):
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def __str__(self):
        """This returns the string representation of an instance"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.size)

    def to_dictionary(self):
        """This function converts the class into a
        dictionary representation"""
        dict = {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
        return dict

