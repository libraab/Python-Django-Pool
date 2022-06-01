#!/usr/local/bin/python3

def your_function():
    f = open("numbers.txt", "r")
    x = f.read()
    y = x.replace(",", "\n")
    print(y, end='')
    f.close()
if __name__ == '__main__':
    your_function()