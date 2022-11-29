#!/usr/bin/python3
def uppercase(str):
    change_case = 0
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            change_case = 32
        else:
            change_case = 0
        print('{:c}'.format(ord(letter) - change_case), end="")
    print()
