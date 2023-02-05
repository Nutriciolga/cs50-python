def main():
    i = input("Input: ")
    print(shorten(i))


def shorten(i):
    for x in i:
        match x.lower():
            case  "a" | "u" | "o" | "i" | "e":
                continue
            case _:
                print(x, end="")
                continue

if __name__ == "__main__":
    main()