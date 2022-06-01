#!/usr/local/bin/python3

def your_function():
    x = int(42)
    print("%s has a type %s" % (x, x.__class__))
    x = "42"
    print("%s has a type %s" % (x, x.__class__))
    x = "quarante-deux"
    print("%s has a type %s" % (x, x.__class__))
    x = float(42.0)
    print("%s has a type %s" % (x, x.__class__))
    x = True
    print("%s has a type %s" % (x, x.__class__))
    x = [42]
    print("%s has a type %s" % (x, x.__class__))
    x = {42: 42}
    print("%s has a type %s" % (x, x.__class__))
    x = (42,)
    print("%s has a type %s" % (x, x.__class__))
    x = set()
    print("%s has a type %s" % (x, x.__class__))

if __name__ == '__main__':
    your_function()