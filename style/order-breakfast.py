#!/usr/bin/env python3

import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def order():
    while True:
        breakfast = input(
          "Please place your order. Would you like waffles or pancakes?\n").lower()
        if 'waffles' in breakfast:
            print_pause("Waffles it is!")
            break
        elif 'pancakes' in breakfast:
            print_pause('Pancakes it is!')
            break
        else:
            print_pause("Sorry I did not understand that.")

    print_pause('Your order will be ready shortly.')


def main():
    print_pause('Hello! I am Bob, the Breakfast Bot.')
    print_pause('Today we have two breakfasts available.')
    print_pause('The first is waffles with strawberries and whipped cream.')
    print_pause('The second is sweet potato pancakes with butter and syrup.')

    order()
    while True:
        new_order = input(
          "Would you like to place another order? Please say 'yes' or 'no'.\n").lower()
        if 'no' in new_order:
            print_pause("OK. goodbye!")
            break
        elif 'yes' in new_order:
            print_pause("Very good, I'm happy to take another order.")
            order()
        else:
            print_pause("Sorry, I don't understand.")
            continue

if __name__ == '__main__':
    main()
