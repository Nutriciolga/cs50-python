# creating the dictionary where each dish is connected with its price
dishes = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
d = 0
# creating an endless loop
while True:
    # requiring the user's input ignoring the case
    try:
        i = input("Item: ").lower()
    # creating an exception when the user inputs "control-d" combination
    except EOFError:
        break
    # creating an exception when the user inputs other item (not from our dictionary)
    except KeyError:
        pass
    # creating condition - comparing item from user's input with the dictionary
    if i in dishes:
        # summing the price of dishes
        d += dishes[i]
        # printing result
        print(f"Total: ${d:.2f}")