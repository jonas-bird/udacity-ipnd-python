#!/usr/bin/env python3
# Rude words detector, version 0.2

import string

rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]


def check_line(line):
    count = 0
    words = line.split(" ")
    for word in words:
        word = word.strip(string.punctuation).lower()
        if word in rude_words:
            count += 1
            print(f"Found rude word: {word}")
    return count


def check_file(filename):
    with open(filename) as myfile:
        rude_count = 0
        for line in myfile:
            rude_count += check_line(line)
    if rude_count == 0:
        print("Congratulations, your file has no rude words.")
        print("At least, no rude words I know.")


def bleep(bad_word):
    # censor words
    index = 0
    for letter in bad_word:
        if letter not in string.punctuation:
            bad_word = bad_word.replace(bad_word)[index], '*')
            index += 1
    return bad_word


if __name__ == "__main__":
    check_file("my_other_story.txt")
