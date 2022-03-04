#!/usr/bin/env python3

import time



def order():
    while True:
        breakfast = input(
          "Please place your order. Would you like waffles or pancakes?\n").lower()
        if 'waffles' in breakfast:
            print("Waffles it is!")
            time.sleep(1)
            break
        elif 'pancakes' in breakfast:
            print('Pancakes it is!')
            time.sleep(1)
            break
        else:
            print("Sorry I did not understand that.")

    print('Your order will be ready shortly.')


def main():
    print('Hello! I am Bob, the Breakfast Bot.')
    time.sleep(2)
    print('Today we have two breakfasts available.')
    time.sleep(2)
    print('The first is waffles with strawberries and whipped cream.')
    time.sleep(2)
    print('The second is sweet potato pancakes with butter and syrup.')

    order()
    while True:
        new_order = input(
          "Would you like to place another order? Please say 'yes' or 'no'.\n").lower()
        if 'no' in new_order:
            print("OK. goodbye!")
            time.sleep(2)
            break
        elif 'yes' in new_order:
            print("Very good, I'm happy to take another order.")
            time.sleep(2)
            order()
        else:
            print("Sorry, I don't understand.")
            continue

if __name__ == '__main__':
    main()
