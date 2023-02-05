# declaration of the function convert
def convert(time):
    # deeds with str variable
    hours, minutes = time.split(":")
    # converting splitted variables from strings into integers
    hours = int(hours)
    a = int(minutes)/60
    # converting variable "time" into float variable
    time = float(hours+a)
    # returning the meaning of the variable "time"
    return time


# the main function
def main():
    # inputting time in 24 hours format divided with ":"
    time = input("What time is it? ")
    # mentioning of the other function
    time = convert(time)
    # comparing given time with time frames for meals, printing results
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


# this line means that the main function of the program starts under this condition
if __name__ == "__main__":
    main()