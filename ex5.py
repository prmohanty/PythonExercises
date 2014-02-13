#!/usr/bin/env python

"""
Write a function translate() that will translate a text into "rovarspraket" (Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between.
For example, translate("this is fun") should return the string "tothohisos isos fofunon".
"""

from ex4 import is_vowel


def translate(string):
    results = []
    for word in string.split():
        result = ''
        for char in word:
            if not is_vowel(char):
                result += char + 'o' + char
            else:
                result += char
        results.append(result)
    return ' '.join(results)


if __name__ == "__main__":
    print translate("this is fun")