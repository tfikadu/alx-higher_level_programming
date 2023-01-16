#!/usr/bin/python3
""" Rectangle Class """


from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width Getter - Read Value """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter width - change value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height Getter - Read Value """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter height - change value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ x Getter - Read Value """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter x - change value """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ y Getter - Read Value """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter y - change value """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Math Area """
        return (self.__height * self.__width)

    def display(self):
        """ Display Rectangle """
        myhash = "#"
        if self.width == 0 or self.height == 0:
            return
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x, end='')
            print(myhash * self.width)

    def update(self, *args, **kwargs):
        """ args Rectangle """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.width = j
                elif i == 3:
                    self.x = j
                elif i == 4:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """ Str format """
        st = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        st = st.format(self.id, self.x, self.y, self.width, self.height)
        return st

    def to_dictionary(self):
        """ Dictionary of rectangle """
        recdic = {"id": self.id, "width": self.width, "height": self.height,
                     "x": self.x, "y": self.y}
        return recdic
