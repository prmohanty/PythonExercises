#!/usr/bin/env python

"""
Write a program that given a text file will create a new text file in which all the lines from the original file are
numbered from 1 to n (where n is the number of lines in the file).
"""


def numbered_file(filepath):
    file_in = open(filepath)
    file_out = open('io_files/ex37_out.txt', 'w')
    for line, content in enumerate(file_in):
        file_out.write('%s %s' % (line + 1, content))


if __name__ == "__main__":
    numbered_file('io_files/ex37.txt')