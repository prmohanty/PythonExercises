#!/usr/bin/env python

"""
Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths
of the word tokens in the text, divided by the number of word tokens).
"""

import re


def avg_word_length(filepath):
    file = open(filepath)
    words = re.findall('\w+', file.read())
    return sum([len(word) for word in words]) / len(words)


if __name__ == "__main__":
    print avg_word_length('io_files/ex38.txt')
