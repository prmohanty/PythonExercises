#!/usr/bin/env python

"""
The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three
numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how
many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.
This is the second change i made.
"""


def max_in_list(li):
    max = li[0]
    for n in li:
        if n > max:
            max = n
    return max


if __name__ == "__main__":
    print max_in_list([1, 2, 5, 3])