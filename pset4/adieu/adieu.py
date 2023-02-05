# In a file called adieu.py, implement a program that prompts the user for names,
# one per line, until the user inputs control-d. Assume that the user will input
# at least one name. Then bid adieu to those names, separating two names with one and,
# three names with two commas and one and, and  names with  commas and one and, as in the below:

# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa


list = []
num = 0
while True:
    try:
        list.append(input("Name: "))
        num += 1
    except EOFError:
        if num == 1:
            print("\nAdieu, adieu, to", *list)
            break
        elif num == 2:
            first = list.pop(0)
            last = list.pop()
            print("\nAdieu, adieu, to " + first, "and " + last)
            break
        else:
            first = list.pop(0)
            last = list.pop()
            print("\nAdieu, adieu, to " + first, *list, "and " + last, sep=", ")
            break