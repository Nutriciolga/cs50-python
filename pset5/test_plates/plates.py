def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    chars = len(s)

    if chars < 2 or chars > 6:
        return False

    if not s[:2].isalpha():
        return False

    digit_count = 0
    for c in s[2:]:
        if c.isdigit():
            digit_count += 1

            if digit_count == 1 and c == "0":
                return False

        elif c.isalpha():
            if digit_count > 0:
                return False

        else:
            return False

    return True


if __name__ == "__main__":
    main()