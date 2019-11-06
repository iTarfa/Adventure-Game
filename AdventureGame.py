import time
import random
import sys


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You are lucked in a room with your friend!")
    print_pause("in front of you there are 2 escape doors.")
    print_pause("only one person can use each door")
    print_pause("but! both doors has a puzzle must be solved to be open!")
    print_pause("your friend decided to flip a coin to choose the door.")
    print_pause("if it's heads, "
                "he get the right room and you get the left room")
    print_pause("if it's tails, "
                "he get the left room and you get the right room")


def coin_flip():
    flip = random.choice(['heads', 'tails'])
    if flip == 'heads':
        print_pause("\nit's heads!")
        left_room()
    else:
        print_pause("\nit's tails!")
        right_room()


def play():
    intro()
    coin_flip()


def right_room():
    print_pause("You got the right room!")
    print_pause("The puzzle appeard in front of you!")

    def puzzle1():
        while True:
            answer = input("16, 23, 19, 19, 22, 15, 25, ? \n"
                           "What number should replace the question mark?\n")
            if "11" in answer:
                print_pause("Your answer is correct! \n"
                            "you can escape now!\n")
                play_again()
            else:
                print_pause("Wrong answer! try again.")
                puzzle1()
    puzzle1()


def left_room():
    print_pause("You got the left room!")
    print_pause("The puzzle appeard in front of you!")

    def puzzle2():
        while True:
            answer = input("25, 50, 27, 46, 31, 38, 39, ? \n"
                           "What number continues the sequence?\n")
            if "22" in answer:
                print_pause("Your answer is correct! \n"
                            "you can escape now!\n")
                play_again()
            else:
                print_pause("Wrong answer! try again.")
                puzzle2()
    puzzle2()


def play_again():
    again = input("Would you like to play again?\n"
                  "Please say yes or no.\n")
    if "no" in again:
        print_pause("Ok, goodbye!")
        sys.exit()
    elif "yes" in again:
        print_pause("Very good, here we go again!\n")
        play()
    else:
        print_pause("I didn't get that sorry")
        play_again()


play()
