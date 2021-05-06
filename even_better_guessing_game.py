#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program is a better guessing number game

import random


def main():
    print("Try to guess a number from 0 to 9:")

    number_random = random.randint(0, 9)
    number_input = input()

    try:
        number_integer = int(number_input)

        if number_integer == number_random:
            print("\nCongratulations, guessed right!")
        else:
            print("\nSorry, guessed wrong! The right number was {}"
                  .format(number_random))
    except Exception:
        print("\nThis input is invalid, please, insert an integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
