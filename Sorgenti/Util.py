# coding: utf-8
from Markets import Markets

global K

global Q

global T

global N #numero di soluzioni nell'intorno

global TABULISTDIM

global inputFile
inputFile="input.txt"


def cost(markets):
    cost = 0    
        
    for t in range(T):
        value=0 #variabile che tiene conto del carico sul camion nel singolo periodo t
	for h in range(K):
            if (markets[h].x[t] != 0):
                cost = cost + 1
		value=value+markets[h].x[t]
        if (value>Q): #controllo se supero la capacità del camion, se si aumento il costo
            cost=cost+1    

    
    return cost


def ReadFile():
  
    try:
	    markets=[]
	    in_file = open(inputFile,"r")
	    line = in_file.readline()   #prima linea inutile che rappresenta il commento
	    ct=0
	    while ct < K:
		line = in_file.readline()
		#print line
		a = line.split(' ')
		m=Markets(a[1], a[2], a[3:(int(T)+3)])  #mi creo l'oggetto market
		markets.append(m)              #appendo alla lista
		ct+=1
	    in_file.close()
    
    except Exception as e:
	print e
    
    finally:
	return markets
