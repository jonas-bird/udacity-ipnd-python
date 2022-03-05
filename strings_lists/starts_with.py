#!/usr/bin/env python3

# # Add your function definition here
# def starts_with(word1, word2):
#     return word1[0] == word2[0]
# # A call like this should return True:
# print(starts_with("banana", "bread"))

# # And one like this should return False:
# print(starts_with("zebonkey", "kiwi"))

# version 2


# def starts_with(long_string, short_string):
#     """takes a long strting and a short string and returns true if the long
#     string begins with the short string
#     """

#     for i, letter in enumerate(short_string):
#         if letter != long_string[i]:
#             return False
#     return True
# probably less efficient than the version that just uses len, why am I
# breaking out the letter at position really?

def starts_with(long, short):
    """string slicing version"""
    return long[0:len(short)] == short
