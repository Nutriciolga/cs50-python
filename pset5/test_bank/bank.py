def main():
    i = input("Greeting: ")
    print(f"${value(i)}")


def value(i):
    i = i.strip().lower()

    if i[0: 5] == "hello": # checking if the greeting is "hello"
        g = 0 # the amount of payment
    elif i[0] == "h": # checking if the greeting starts from "h"
        g = 20 # the amount of payment
    else: # the case when the greeting is not "hello" and not starts from "h"
        g = 100 # the amount of payment should be integer!

    return g


if __name__ == "__main__": 
    main()