#!/usr/bin/env python

"""
Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False
otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should
(also) write it using two nested for-loops.
This is the First Change I Made. 
"""


def overlapping(li1, li2):
    for elem1 in li1:
        for elem2 in li2:
            if elem1 == elem2:
                return True
    return False


if __name__ == "__main__":
    print overlapping([1, 2], [3, 4])
    print overlapping([1, 2], [2, 3])
    print overlapping(['a', 'b', 'c'], ['c', 'd'])
