#!/usr/bin/env python3

import time


def print_pause(msg):
    """Takes a parameter, prints it, and waits 2 seconds"""
    print(msg)
    time.sleep(2)


def validate_input(prompt, possible_choices):
    """
    Prompts the user for a response and checks if the input is in a list
    provided by the second parameter
    """
    while True:
        answer = input(prompt)
        for option in possible_choices:
            if option in answer:
                return option

        print_pause("Sorry, I don't understand.")


print_pause("Hello! I am Bob, the Breakfast Bot.")
print_pause("Today we have two breakfasts available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")

while True:
    valid_choices = ['waffles', 'pancakes']
    prompt = "Please place your order. Would you like waffles or pancakes?\n"
    choice = validate_input(prompt, valid_choices)
    print_pause(f"{choice} it is!")
    print_pause("Your order will be ready shortly.")
    again_choices = ['yes', 'no']
    prompt_again = "Would you like to place another order? Please say 'yes' or 'no'.\n"
    order_again = validate_input(prompt_again, again_choices)
    if order_again == 'no':
        print_pause("OK, goodbye!")
        break
    print_pause("Very good, I'm happy to take another order.")
