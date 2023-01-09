#!/usr/bin/python3
"""
MyList class module.
Define MyList class.
"""


class MyList(list):
    """Define a MyList."""

    def print_sorted(self):
        """Print the list sorted"""
        print(sorted(self))
