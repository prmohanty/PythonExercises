#!/usr/bin/env python

"""
Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a frequency
listing of the characters contained in the file, and prints a sorted and nicely formatted character frequency table to
the screen.
"""

import re


def char_freq_table(filepath):
    file = open(filepath)
    chars = file.read().lower().replace(" ", "").replace("\n", "")
    freqs = {key: 0 for key in chars}
    for char in chars:
        freqs[char] += 1
    for word in freqs:
        print "%s: %s" % (word, freqs[word])


if __name__ == "__main__":
    char_freq_table('io_files/ex34.txt')