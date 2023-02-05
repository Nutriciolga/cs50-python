# inputting expression dividing by spaces
i = input("Expression: ")
# splitting into three components
x, y, z = i.split()
# the first and the third symbols are integers
x = int(x)
z = int(z)
# identifying mathematical action sign and printing results
match y:
    case "+":
        print(float(x+z))
    case "-":
        print(float(x-z))
    case "*":
        print(float(x*z))
    case "/":
        if z != 0:
            print(round(x/z, 1))
