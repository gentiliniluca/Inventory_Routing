import itertools

x = {}
x['t0'] = 5

a = x['t0']
b = 0
count = 0
while(a >= 0):
    b = x['t0'] - a
    while(b >= 0):
        c = x['t0'] - a - b
        while(c >= 0):
            d = x['t0'] - a - b - c
            print a, b, c, d
            c = c - 1
        b = b - 1
    a = a - 1