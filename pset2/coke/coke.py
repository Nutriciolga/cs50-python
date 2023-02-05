due = 50
change = 0
# creating unlimited loop
while True:
    # printing amount due
    print("Amount due: " + str(due))
    # inputting integer variable
    n = int(input("Insert Coin: "))
    # comparing variable with our values
    match n:
        case 25 | 10 | 5:
            # checking if the amount is less then tje price
            if n < due:
                # calculating the amount due
                due -= n
            else:
                # calculating the amount change
                change = n - due
                break

# printing the change
print("Change Owed: " + str(change))
