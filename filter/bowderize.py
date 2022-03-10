#!/usr/bin/env python3
# Rude words detector, version 0.2

import string

rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]


def check_line(line):
    count = 0
    words = line.split(" ")
    fixed_words = []
    for word in words:
        checkword = word.strip(string.punctuation).lower()
        if checkword in rude_words:
            count += 1
            print(f"Found rude word: {word}")
            word = bleep(word)
        fixed_words.append(word)
    line = " ".join(fixed_words)
    return line, count


def check_file(filename):
    with open(filename) as myfile:
        rude_count = 0
        new_lines = []
        for line in myfile:
            line, rude_sub = check_line(line)
            rude_count += rude_sub
            new_lines.append(line)

    if rude_count == 0:
        print("No banned words found.")
    else:
        # create new file for censored version
        with open("bowderized.txt", "w") as bleeped:
            bleeped.write("\n".join(new_lines))
        print(f"{rude_count} words censored. See bowderized.txt for the"
              "version with them hidden")


def bleep(bad_word):
    # censor words
    index = 0
    for letter in bad_word:
        if letter not in string.punctuation:
            bad_word = bad_word.replace(bad_word[index], '*')
            index += 1
    return bad_word


if __name__ == "__main__":
    check_file("my_story.txt")
    check_file("my_other_story.txt")
