#!/usr/bin/env python

"""
Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line
to the screen if it is a palindrome.
"""

from ex17 import is_palindrome_extended


def palidrome_file(filepath):
    file = open(filepath)
    for line in file.read().split("\n"):
        if is_palindrome_extended(line):
            print line


if __name__ == "__main__":
    palidrome_file('io_files/ex32.txt')