def main():
    i = input("Input: ")
    print(shorten(i))


def shorten(i):
    s = ""
    for x in i:
        match x.lower():
            case  "a" | "u" | "o" | "i" | "e":
                continue
            case _:
                s += x
                continue
    return s

if __name__ == "__main__":
    main()