# In a file called professor.py, implement a program that:

# Prompts the user for a level, . If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = ,
# wherein each of X and Y is a non-negative integer with  digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problem. If an answer is not correct
# (or not even a number), the program should output EEE and prompt the user again,
# allowing the user up to three tries in total. If the user has still not answered
# correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score, a number out of 10.
# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts)
# the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly
# generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        rn1, rn2 = generate_integer(level)
        ans = rn1 + rn2

        for e in range(3):
            print(f'{rn1} + {rn2} = ', end='')

            try:
                i = int(input())
            except ValueError:
                i = -1

            if i == ans:
                score += 1
                break
            else:
                print("EEE")
                if e == 2:
                    print(f'{rn1} + {rn2} = {ans}', end='')

    print("Score:", score)
    exit(0)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                break
        except ValueError:
            pass
    return level


def generate_integer(level):
    match level:
        case 1:
            lower = 0
            higher = 9
        case _:
            lower = 10**(level - 1)
            higher = 10**(level) - 1

    rn1 = random.randint(lower, higher)
    rn2 = random.randint(lower, higher)
    return rn1, rn2


if __name__ == "__main__":
    main()