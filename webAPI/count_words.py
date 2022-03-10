#!/usr/bin/env python3

# Simple word count refresher


my_str = 'it appears that the the appears the most in the sentence'
my_dict = {}

my_words = my_str.split()
for word in my_words:
    my_dict[word] = my_dict.get(word, 0) + 1

for k, v in my_dict.items():
    print(f"\'{k}\' appears {v} time(s) in the string")
