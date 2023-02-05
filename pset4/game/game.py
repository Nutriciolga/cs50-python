# In a file called game.py, implement a program that:
# Prompts the user for a level, . If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and , inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.

while True:  # creating the endless loop where the user inputs integer positive variable
    try:
        i = int(input("Level: "))
        if i > 0:  # checking if the input is correct
            import random  # generating new variable between 1 and user's input
            number = random.randint(1, i)
            while True:  # creating the endless loop where user should input an integer variable
                try:
                    g = int(input("Guess: "))

                    if g < number:  # checking whether user's input is less than random number
                        print("Too small!")
                        pass  # prompting user new attempt
                    elif g > number:  # checking whether user's input is more than random number
                        print("Too large!")
                        pass  # prompting user new attempt
                    elif g == number:  # checking whether user's input is equal the random number
                        print("Just right!")
                        exit()

                except ValueError:  # in case of ValueError prompting user new attempt
                    pass

    except ValueError:
        pass
