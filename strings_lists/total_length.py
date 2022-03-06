#!/usr/bin/env python3


def total_length(list_o_strings):
    accumulator = 0
    for item in list_o_strings:
        accumulator += len(item)

    return accumulator
