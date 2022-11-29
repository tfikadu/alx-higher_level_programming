#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -2):
    print('{:c}{:c}'.format(letter, letter - 33), end='')
