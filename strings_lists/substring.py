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


def locate_first(string, target):
    """
    Find the first occurence of string in target and return the
       index of the start position of the substring or -1 if the
       the string does not occur as a substring of the target
    """
    index = 0
    while index < len(string):
        if string[index: index + len(target)] == target:
            return index
        index += 1
    return -1


def locate_all(string, target):
    """
    Return a list of the indexes of the start positions of all
    occurences of string in target
    """
    matches = []
    index = 0
    while index < len(string):
        if string[index: index + len(target)] == target:
            matches.append(index)
            index += len(string)
        else:
            index += 1
    return matches
