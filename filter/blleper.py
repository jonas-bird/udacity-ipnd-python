#!/usr/bin/env python3

"""Function to censor words by replacing characters with *"""

import string


def bleep(bad_word):
    # censor words
    index = 0
    for letter in bad_word:
        if letter not in string.punctuation:
            bad_word = bad_word.replace(bad_word)[index], '*')
            index += 1
    return bad_word


test_words = ["crap", "darn!", "Heck!!!", "jerk...", "idiot?", "butt", "devil"]
for word in test_words:
    print(bleep(word))
