#!/usr/bin/env python3

import random
import words


def silly_string(nouns, verbs, templates):
    """Create a mad-lib from lists of nound, verbs, and templates"""
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0

    # Add a variable with the length of the placeholders
    place_hold = len('{{noun}}')

    # Add a while loop here.
    while index < len(template):
        if template[index : index + place_hold] == '{{noun}}':
            output.append(random.choice(nouns))
            index += place_hold
        elif template[index : index + place_hold] == '{{verb}}':
            output.append(random.choice(verbs))
            index += place_hold
        else:
            output.append(template[index])
            index += 1

    # After the loop has finished, join the output and return it.
    return "".join(output)


# To see the results, we need to call the funtion and print what it returns:
print(silly_string(words.nouns, words.verbs, words.templates))
