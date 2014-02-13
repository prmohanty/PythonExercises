#!/usr/bin/env python

"""
Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it.
Represent the frequency listing as a Python dictionary.
Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
"""


def char_freq(string):
    freq = {key: 0 for key in string}
    for i in string:
        freq[i] += 1
    return freq


if __name__ == "__main__":
    print char_freq("abbabcbdbabdbdbabababcbcbab")
