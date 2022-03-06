#!/usr/bin/env python3

def breakify(some_text):
    return " <br> ".join(some_text)


def remove_SPAM(string):

    output = []
    index = 0
    while index < len(string):
        if string[index:index+5] == 'SPAM!':
            index += 5
        else:
            output.append(string[index])
            index += 1
    print("".join(output))
