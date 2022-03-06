#!/usr/bin/env python3

import time


items = []


def pause_print(string, delay):
    print(string)
    time.sleep(delay)


def lobby():
    pause_print("You push the button for the first floor.", 2)
    pause_print("After a few moments, you find "
                "yourself in the lobby.", 2)
    if 'ID card' in items:
        pause_print("The clerk greets you, but she has already given you your"
                    "ID card, so there is nothing more to do here now.", 2)
    else:
        items.append('ID card')
        pause_print("The clerk greets you and gives you your ID card." ,2)
    choose()


def hr():
    pause_print("You push the button for the second floor.", 2)
    pause_print("in the human resources department.", 2)
    if 'handbook' in items:
        pause_print("The HR folks are busy at their desks.", 2)
        pause_print("There doesn't seem to be much to do here.", 2)
    else:
        pause_print("The head of HR greets you.", 2)
        if 'ID card' in items:
            pause_print("He looks at your ID card and then gives"
                        "you a copy of the employee handbook.", 2)
            items.append('handbook')
        else:
            pause_print("He has something for you, but says he can't "
                        "give it to you until you go get your ID card.", 2)
    pause_print("You head back to the elevator.", 2)
    choose()


def engineering():
    pause_print("You push the button for the third floor.", 2)
    pause_print("After a few moments, you find yourself "
                "in the engineering department.", 2)
    pause_print("")
    if 'ID card' not in items:
        pause_print("Unfortunately, the door is locked and you can't get in."
                    "It looks like you need some kind of key card to open the door.", 2)
        pause_print("You head back to the elevator.", 2)
        choose()
    else:
        pause_print("You use your ID card to open the door.", 2)
        pause_print("Your program manager greets you and tells you"
                    "that you need to have a copy of the employee"
                    "handbook in order to start work.", 2)
        if 'handbook' not in items:
            pause_print("They scowl when they see that you don't have it, and"
                        "send you back:w
                        to the elevator.", 2)
            choose()
        else:
            pause_print("Fortunately, you got that from HR!", 2)
            pause_print("Congratulatons! You are ready to start your new job as"
                        "vice president of engineering!", 2)

def choose():
    pause_print("Please enter the number for the "
                "floor  you would like to visit:", 2)
    destination = input("1. Lobby\n"
                        "2. Human resources\n"
                        "3. Engineering department\n")
    if destination == '1':
        lobby()
    elif destination == '2':
        hr()
    elif destination == '3':
        engineering()
    else:
        choose()


def intro():
    pause_print("You have just arrived at your new job!", 2)
    pause_print("You are in the elevator.", 2)


def main():
    intro()
    choose()


if __name__ == '__main__':
    main()
