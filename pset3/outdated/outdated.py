# creating a dictionary with the names of months and their nums
dict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


# creating endless loop checking conditions
while True:
    try:
        i = input("Date: ").strip()  # inputting the date ingnoring white spaces
        if i[0].isalpha() and i.find(",") != -1:  # checking two conditions for input with letters
            i = i.replace(",", "")  # deleting the comma
            x, y, z = i.split()  # splitting into three parts
            day = int(y)  # checking if the number of days is available in other case reprompt
            if day > 31:
                raise KeyError
            break
        elif i[0].isdecimal() and i.find("/") != -1:  # checking two conditions for input with digits
            i = i.replace("/", " ")
            x, y, z = i.split()  # splitting into three parts
            m = int(x)  # converting into integers month and day
            day = int(y)
            if m > 12 or day > 31:  # checking if the number of days and month is available in other case reprompt
                raise KeyError
            break

    except ValueError:  # evaluating ValueError in the case of incorrect order of input
        pass

    except KeyError:  # evaluating KeyError in the case of incorrect order of input
        pass

month = x
year = z
if day < 10:
    day = y.zfill(2)  # if the day is one digit printing it with the zero before (for integers)
else:
    day = y
if month in dict:
    month = (f"{dict[month]:02}")  # if the month is one digit printing it with the zero before (for symbols from the dictionary)
else:
    m = int(x)
    if m < 10:
        month = x.zfill(2)  # if the day is one digit printing it with the zero before (for integers)

# printing the string in international standard order
print(year + "-" + month + "-" + day)

