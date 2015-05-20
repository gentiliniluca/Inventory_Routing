# coding: utf-8

#from Markets import Markets

global K
K=4

global Q

global T
T=5

global N #numero di soluzioni nell'intorno

global TABULISTDIM

global inputFile
inputFile="input.txt"


def cost(markets):
    cost = 0    
        
    for t in range(T):
        value = 0 #variabile che tiene conto del carico sul camion nel singolo periodo t
        for h in range(K):
            if(markets[h].x[t] != 0):
                cost = cost + 1
                value = value + markets[h].x[t]
        if(value > Q): #controllo se supero la capacità del camion, se si aumento il costo
            cost = cost + 1
             
    return cost


