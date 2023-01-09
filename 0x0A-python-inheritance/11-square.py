#!/usr/bin/python3
'''
 Import statement
 '''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Rectangle class
    '''

    def __init__(self, size):
        """ Doctring """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        '''
        String rep
        '''
        return ("[Square] {}/{}".format(self.__size, self.__size))
