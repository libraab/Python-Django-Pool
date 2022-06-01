#!/usr/local/bin/python3

def your_function():
    d = {
        'Hendrix' : '1942',
        'Allman' : '1946',
        'King' : '1925',
        'Clapton' : '1945',
        'Johnson' : '1911',
        'Berry' : '1926',
        'Vaughan' : '1954',
        'Cooder' : '1947',
        'Page' : '1944',
        'Richards' : '1943',
        'Hammett' : '1962',
        'Cobain' : '1967',
        'Garcia' : '1942',
        'Beck' : '1944',
        'Santana' : '1947',
        'Ramone' : '1948',
        'White' : '1975',
        'Frusciante': '1970',
        'Thompson' : '1949',
        'Burton' : '1939',
        }
        
    y = sorted(d.items(), key=lambda x: x[1])

    new = {}
    for h, g in y:
        new.setdefault(g, []).append(h)

    for a, b in new.items():
        b = sorted(b)
        for c in b:
            print('%s ' % (c), end='')
        print()
        
if __name__ == '__main__':
    your_function()