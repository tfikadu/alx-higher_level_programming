#!/usr/bin/python3
'''
Write a function that writes an
Object to a text file, using a
JSON representation
'''

import json


def save_to_json_file(my_obj, filename):
    '''
    Writes object to text file using JSON
    '''
    if filename is None:
        return
    with open(filename, 'w', encoding='utf-8') as f:
        json_var = json.dump(my_obj, f)
