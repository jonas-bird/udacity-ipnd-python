#!/usr/bin/env python3

import time


def print_pause(msg):
    print(msg)
    time.sleep(2)


print_pause("Hello! I am Bob, the Breakfast Bot.")
print_pause("Today we have two breakfasts available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")

while True:
    while True:
        response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print_pause("Waffles it is!")
            break
        elif "pancakes" in response:
            print_pause("Pancakes it is!")
            break
        else:
            print_pause("Sorry, I don't understand.")
    print_pause("Your order will be ready shortly.")
    while True: # We want to loop until they enter a valid response.
        order_again = input("Would you like to place another order? Please say 'yes' or 'no'.\n").lower()
        if 'no' in order_again:
            print_pause("OK, goodbye!")
            break # Note that this will only break out of the inner loop.
        elif 'yes' in order_again:
            print_pause("Very good, I'm happy to take another order.")
            break # Again, this only breaks out of the inner loop.
        else:
            print_pause("Sorry, I don't understand.")
    if 'no' in order_again:
        break # We need this last break statement to exit the outer loop.
