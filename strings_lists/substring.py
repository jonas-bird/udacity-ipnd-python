#!/usr/bin/env python3

def is_substring(a_substring, a_string):

    length = len(a_substring)
    for i in range(len(a_string) - length):
        if a_string[i:i+length] == a_substring:
            return True
    return False


def count_substring(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index:index+len(target)] == target:
            total += 1
            index += len(target)
        else:
            index += 1
    return total
