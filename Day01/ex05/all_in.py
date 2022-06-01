#!/usr/local/bin/python3

import sys
def us(str):
    if (str.isspace()):
        return
    print (str.strip() + " is neither a capital city nor a state")

def is_cap(states, capital_cities, i):
    for a, b in capital_cities.items():
        if (b.lower() == i.strip().lower()):
            for key, value in states.items():
                if (value == a):
                    print(i.title().strip() + " is the capital of " + key)
                    return(1)
    return(0)

def is_state(states, capital_cities, i):
    for key, value in states.items():
        if (key.lower() == i.strip().lower()):
            for a, b in capital_cities.items():
                if(value == a):
                    print(b + " is the capital of " + i.title().strip())
                    return(1)
    return(0)

def your_function():
    if ((len(sys.argv) != 2) or (sys.argv[1].find(",,") != -1)):
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
    x = sys.argv[1].split(",")

    for i in x:
        if(is_cap(states, capital_cities, i) == False):
            if(is_state(states, capital_cities, i) == False):
                us(i)
if __name__ == '__main__':
        your_function()