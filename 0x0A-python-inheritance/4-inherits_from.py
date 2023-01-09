#!/usr/bin/python3
'''
Write a function that returns True
if the object is an instance of a class
that inherited
'''


def inherits_from(obj, a_class):
    '''
    Method returns True if is inherited
    '''
    return isinstance(obj, a_class) and type(obj) is not a_class
