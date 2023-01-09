#!/usr/bin/python3
'''
Write a class MyInt that inherits from int
'''


class MyInt(int):

    def __eq__(self, value):
        return int(self) != int(value)

    def __ne__(self, value):
        return int(self) == int(value)
