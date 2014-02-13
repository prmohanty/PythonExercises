#!/usr/bin/env python

"""
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
For example, is_palindrome("radar") should return True.
"""


def is_palindrome(string):
    return string == string[::-1]


if __name__ == "__main__":
    print is_palindrome("aabbaa")
    print is_palindrome("abc")
    print is_palindrome("radar")