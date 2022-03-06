#!/usr/bin/env python3

def until_dot(some_string):
    """function that takes a string and returns the portion before the period
    """

    i = 0
    before_dot = ""
    while i < len(some_string):
        if some_string[i] == '.':
            break
        before_dot += some_string[i]
        i += 1
    if some_string == before_dot:
        return "No dots here"
    return before_dot
# You can test your function using the print statements below:

# This should print 'Udacity'
print(until_dot("Udacity.com"))

# This should print 'This is a sentence'
print(until_dot("This is a sentence. This is another."))

# This should print '192'
print(until_dot("192.168.200.2"))

# This should print 'no dots here'
print(until_dot("Is there a dot?"))
