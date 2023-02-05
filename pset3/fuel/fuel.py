# creating endless loop
while True:
    # inputting and splitting by "/" and checking variables
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        # calculating the percentile of fuel in tank
        z = x/y*100
        # checking the fuel (shouldn't be more than volume of the tank)
        if x > y:
            # calling the error by name (assigning the name of error to our condition)
            raise ValueError
    # continue the loop after finding exception
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        break
# creating the condition for the percentile of the fuel
if 1 < z < 99:
    # printing the result rounding it, avoiding the space between %
    print(f"{round(z)}%")
elif 100 >= z >= 99:
    print("F")
elif z <= 1:
    print("E")