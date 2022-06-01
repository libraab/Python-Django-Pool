#!/usr/local/bin/python3

import sys
def us():
    print ("Unknown capital city")

def your_function():
    if (len(sys.argv) != 2):
        return
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    for a, b in capital_cities.items():
        if (b == sys.argv[1]):
            for key, value in states.items():
                if (value == a):
                    print(key)
                    exit()
    else:
        us()
        exit()
if __name__ == '__main__':
        your_function()