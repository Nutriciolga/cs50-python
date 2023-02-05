# inputting the greeting, removing whitespace
i = input("Greeting: ").strip()
# comparing first 5 letters of the greeting
if i[0: 5] == "hello" or i[0: 5] == "Hello":
    # printing "award" if it matches
    print("$0")
    # comparing the first letter of the greeting
elif i[0] == "h" or i[0] == "H":
    # printing "award" if it matches
    print("$20")
else:
    # printing "award" if it matches
    print("$100")