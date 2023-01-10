#!/usr/bin/python3
"""This module adds arugments to a Python list then saves it to a JSON file"""
import json
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'
try:
    new_list = load_from_json_file(filename)
except (ValueError, FileNotFoundError):
    new_list = []

new_list = new_list + argv[1:]
save_to_json_file(new_list, filename)
