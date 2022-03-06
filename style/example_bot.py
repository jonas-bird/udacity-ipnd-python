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
        answer = input(prompt).lower()
        for option in possible_choices:
            if option in answer:
                return option

        print_pause("Sorry, I don't understand.")


def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")


def get_order(menu_options):
    prompt = "Please place your order. Would you like "
    prompt += " or ".join(menu_options) + "\n"
    choice = validate_input(prompt, menu_options)
    print_pause(f"{choice} it is!")
    print_pause("Your order will be ready shortly.")
    order_again(menu_options)


def order_again(menu_options):
    again_choices = ['yes', 'no']
    prompt_again = "Would you like to place another order? Please say 'yes' or 'no'.\n"
    order_again = validate_input(prompt_again, again_choices)
    if order_again == 'yes':
        print_pause("Very good, I'm happy to take another order.")
        get_order(menu_options)
    else:
        print_pause("OK, goodbye!")


def main():
    """run the program"""
    valid_choices = ['waffles', 'pancakes', 'bacon']
    intro()
    get_order(valid_choices)

if __name__ == "__main__":
    main()
