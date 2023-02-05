#In a file called playback.py, implement a program in Python
#  that prompts the user for input and then outputs that same input,
# replacing each space with ... (i.e., three periods).

# Program asks to input text
i = input("Enter your words: ")
# Print words with points between them
print(i.replace(" ", "..."))