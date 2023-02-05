import sys  # reading command from user's output
from pyfiglet import Figlet
fig = Figlet()


def main():  # creating finction getting user's input
    s = input("Input: ")
    return s


def ran():  # creating function executing random choice of font from the library
    import random
    f = random.choice(fig.getFonts())
    fig.setFont(font=f)
    return print(fig.renderText(main()))


if len(sys.argv) == 3:  # checking if the name of font was correctly inputed
    if sys.argv[1] == "-f" and sys.argv[2] in fig.getFonts():
        font = sys.argv[2]
        f = Figlet(font)  # chosing certain font from the library
        print(f.renderText(main()))

    else:
        sys.exit("Invalid usage")

elif len(sys.argv) == 1:  # checking wheether the user didn't input the name of font
    ran()
else:
    sys.exit("Invalid usage")
