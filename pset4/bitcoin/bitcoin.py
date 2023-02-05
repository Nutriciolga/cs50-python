# In a file called bitcoin.py, implement a program that:

# Expects the user to specify as a command-line argument the number
# of Bitcoins, , that they would like to buy. If that argument cannot
#  be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
# which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure
# to catch any exceptions, as with code like:


import requests
import sys

while True:
    try:
        match len(sys.argv):
            case 2:
                f = float(sys.argv[1])
                if f:
                    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                    d = request.json()
                    bitc_price = d['bpi']['USD']['rate_float']
                    amount = f*bitc_price
                    print(f"${amount:,.4f}")
                    break
                else:
                    sys.exit("Command-line argument is not a number")
            case 1:
                sys.exit("Missing command-line argument")
            case _:
                sys.exit("Error")

    except requests.RequestException:
        break