# inputting the line in camel case
i = input("camelCase: ").strip()
# creating the empty variable for result string
s = ""
# the loop for checking each character in the string
for char in i:
    # looking if the current characcter is upper
    if char.isupper():
        # changing the upper case into lower one adding the sign "_"
        char = "_" + char.lower()
    # saving/adding character in the new string
    s += char
# printing the result string
print(s)