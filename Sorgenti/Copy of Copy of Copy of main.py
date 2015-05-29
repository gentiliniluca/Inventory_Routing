import itertools

x = {}
x['t0'] = 100

a = x['t0']
b = 0
count = 0
while(a >= b):
    b = x['t0'] - a
    c = 0
    while(b >= c):
        c = x['t0'] - a - b
        d = 0
        while(c >= d):
            d = x['t0'] - a - b - c
            if((a>=b) and (b>=c) and (c>=d)):
                p = []
                for l in list(itertools.permutations((a, b, c, d))):
                    if(not l in p):
                        p.append(l)
                print p
                count = count + 1
            c = c - 1
        c = 0
        b = b - 1
    b = 0
    a = a - 1
print count