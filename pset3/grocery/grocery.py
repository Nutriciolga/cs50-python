# creating the empty dictionary
groceries = {}
# creating the endless loop
while True:
    # inputting the names of products in any case
    try:
        item_name = input().upper()
    # handling the quit condition
    except EOFError:
        break
    # getting the number of items bound to item name
    num = groceries.get(item_name)
    # if there is an entry with item_name key, num will be a natural integer because we previously entered the data into the dictionary
    if num:
        # incrementing the number of items
        groceries[item_name] = num + 1
    else:
        # initialising item name and number pair
        groceries[item_name] = 1

for item_name in sorted(groceries.keys()):
    print(f'{groceries[item_name]} {item_name}')