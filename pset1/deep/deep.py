# user inputs answer the "big" question
i = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
# comparing the user's answer with "correct" one
match i:
    case "forty two" | "forty-two" | "Forty two" | "Forty-two" | "42" | "FoRty TwO":
        print("Yes")
    # in other cases we print "no"
    case _:
        print("No")