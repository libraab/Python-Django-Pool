#!/usr/local/bin/python3

import sys
def us():
    print ("Unknown state")

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
    for key, value in states.items():
        if (key == sys.argv[1]):
            for a, b in capital_cities.items():
                if (value == a):
                    print(b)
                    exit()
    else:
        us()
        exit()
if __name__ == '__main__':
        your_function()