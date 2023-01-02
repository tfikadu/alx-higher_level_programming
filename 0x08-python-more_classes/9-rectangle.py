#!/usr/bin/python3
"""
Module creates the Rectangle class
"""


class Rectangle:
    """
    Class Rectangle with validated private instance attributes width and height
    Attributes:
        number_of_instances: number of instances of Rectangle
        print_symbol: symbol used for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiates width and height using property setter
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns a string of Rectangle instance using #, empty string"""
        if self.width == 0 or self.height == 0:
            return ""
        row = "{}".format(self.print_symbol) * self.width
        rect = row
        for i in range(self.height - 1):
            rect += "\n" + row
        return rect

    def __repr__(self):
        """Returns a string representation able to create new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Prints 'Bye rectangle...' when instance is deleted"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """width: width of rectangle
        setter validates value is an integer >= 0
        Parameter:
            value: value of the width
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height: height of rectangle
        setter validates value is an integer >= 0
        Parameter:
            value: value of the height
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the calculated area of Rectangle instance"""
        return self.width * self.height

    def perimeter(self):
        """Returns the calculated perimeter of Rectangle instance"""
        if self.height == 0 or self.width == 0:
            return 0
        return (self.width + self.height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger Rectangle or rect_1 if they are equal
        Raises:
            TypeError: if rect_1 or rect_2 is not a Rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns new Rectangle instance with width == height == size
        Parameters:
            size: height and width of new instance
        """
        return cls(size, size)
