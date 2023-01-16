#!/usr/bin/python3
""" Squeare that inherits """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ read size """
        return self.width

    @size.setter
    def size(self, value):
        """size setter """
        self.width = value
        self.height = value

    def __str(self):
        """ Print Method """
        s = "[Square] ({:d}) {:d}/{:d} - {:d}"
        s = s.format(self.id, self.x, self.y, self.width)
        return s

    def update(self, *args, **kwargs):
        """ Updates square """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j

            else:
                if "id" in kwargs:
                    self.id = kwargs["id"]
                if "size" in kwargs:
                    self.size = kwargs["size"]
                if "x" in kwargs:
                    self.x = kwargs["x"]
                if "y" in kwargs:
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary square """
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["size"] = self.size
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
