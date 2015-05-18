from Loads import Loads
from Markets import Markets

global K

global Q

global T

global N #numero di soluzioni nell'intorno

global TABULISTDIM

def cost(markets, load):
    cost = 0
    
    for h in range(K):
        for t in range(T):
            if (markets[h].x[t] != 0):
                cost = cost + 1
    
    for t in range(T):
        if (load.values[t] > Q):
            cost = cost + 1
    
    return cost