# creating dictionary
fruits = {
    "apple": "130",
    "avocado": "50",
    "banana": "130",
    "candaloupe": "50",
    "grapes": "90",
    "grapefruit": "60",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "pear": "100",
    "plums": "70",
    "pineapple": "50",
    "peach": "60",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerin": "50",
    "watermelon": "80"
}
# inputting Item ignoring upper case
i = input("Item: ").lower()
# creating condition - comparing item from user's input with the dictionary
if i in fruits:
    # printing result
    print("Calories:", fruits[i])