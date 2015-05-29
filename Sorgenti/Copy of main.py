# coding: utf-8

import random
import copy
from operator import itemgetter
import time

import Util
import File
from Markets import Markets
from Moves import Moves

start = time.time()
#reperimento dei dati iniziali dal file di input e inizializzazione del problema con una soluzione banale
markets = []
markets = File.readFile()
#for h in range(Util.K):
#    markets.append(Markets(S[h], S1[h], q[h]))
#    
#load = Loads(markets)

#come soluzione si intende la situazione dei supermercati
bestsolution = copy.deepcopy(markets)
bestsolutioncost = Markets.cost(bestsolution)
sk = copy.deepcopy(markets)

#ciclo contenente l'algoritmo
tabulist = []
newneighborhood = True
k = 0
print "\nExecution:  " + "\t",
tmp = -1
while k < Util.ITERATIONS:
    #f = open("output.txt", "a")
    #f.write("K =" + str(k))
    #f.close()
    #print k
    
    
    
    #Un po' di piacere per gli occhi...
    perCent = k*100//Util.ITERATIONS
    if(perCent % 10 == 0 and tmp != perCent):
        if(tmp != -1):
            print " - ",
        print str(perCent) + "%",
        tmp = perCent
    
    
    # selezionare la miglior soluzione dell'intorno, anche peggiore
    # per il momento selezione casuale
    
    #verificare se è necessario lavorare in un nuovo vicinato (lettura del parametro impostato sotto) e che il vicinato attuale contenga almeno un elemento 
    if(newneighborhood):
        for h in range(0, K):
            for t0 in range (0, T):
                y = markets[h].x[t0]
                
                while(y > 0):
                    z = y
                    for t in range(0, T):
                        array = {}
                        array[t0] = True
                        ti = t
                        while(markets[h].x[t0] > 0):
                            if(ti != t0):
                                if(not ti in array):
                                    array[ti] = True
                                    move = Moves(h, t0, ti, z)
                                    if(markets[h].do(move)):
                                        print "da valutare il costo e aggiungere alla tabu move"
                                        z = markets[h].x[t0]
                                    #da valutare il costo e aggiungere alla tabu move
                            ti = (ti + 1) % T
                        markets = sk
                    y = y - 1
            
            
            
            
            
            
        
    #ordinare per costo crescente la lista e prendere il primo elemento (migliore)
    neighborhood = sorted(neighborhood, key = itemgetter(0))
    bestneighborcost, bestneighbor, bestneighbormoves = neighborhood[0]
    
    bestneighbormoveslist = []
    for m in bestneighbormoves:
        bestneighbormoveslist.append(Moves(bestneighbormoves[m].h, bestneighbormoves[m].t, bestneighbormoves[m].t0, bestneighbormoves[m].x))
    
    if(bestneighborcost < bestsolutioncost):
        bestsolution = copy.deepcopy(bestneighbor)
        bestsolutioncost = copy.deepcopy(bestneighborcost)
    else:
        if(Util.subfinder(bestneighbormoveslist, tabulist)):
            newneighborhood = False
            neighborhood.pop(0)
            continue
    
    newneighborhood = True       
    sk = copy.deepcopy(bestneighbor)
    tabulist.extend(bestneighbormoveslist)
    while(len(tabulist) > Util.TABULISTDIM):
        tabulist.pop(0)    
    k = k + 1
print " - 100%\n"
print "Elapsed time:", int(time.time()-start), "seconds\n\nThe best solution is:"

for h in bestsolution:
    print h.toString()
    
print "\nCost: " + str(bestsolutioncost)
#f.write("Cost:" + str(bestsolutioncost))

#f.close()