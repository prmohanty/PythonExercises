#!/usr/bin/env python

"""
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a
language, the works of an author, or in a single text. Define a function that given the file name of a text will return
all its hapaxes. Make sure your program ignores capitalization.
"""

import re


def hapax(filepath):
    file = open(filepath)
    words = re.findall('\w+', file.read().lower())
    freqs = {key: 0 for key in words}
    for word in words:
        freqs[word] += 1
    for word in freqs:
        if freqs[word] == 1:
            print word


hapax('io_files/ex36.txt')