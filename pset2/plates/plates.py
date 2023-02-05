# creating main function which calls additional function which returns True or False
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# creating additional function


def is_valid(s):
    chars = len(s)
    # checking the length of the user's input
    if chars < 2 or chars > 6:
        return False
    # checking the first two characters (letters)
    if not s[:2].isalpha():
        return False
    # checking the rest of the symbols (digits)
    digit_count = 0
    for c in s[2:]:
        if c.isdigit():
            digit_count += 1
            # the first digit shouldn't be 0
            if digit_count == 1 and c == "0":
                return False
        # checking that letters shouldn't be in the middle of digit line
        elif c.isalpha():
            if digit_count > 0:
                return False
        # checking symbols (shouldn't be non letters and non digits)
        else:
            return False
    # returning True if all checkings are passed
    return True


# calling the main function
main()