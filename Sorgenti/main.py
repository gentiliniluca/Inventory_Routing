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
        neighborhood = []
        i = 0
        while i < Util.N:
            #f = open("output.txt", "a")
            #f.write("I =" + str(i))
            #f.close()
            #print "I =" + str(i) #la probabilità di due soluzioni uguali è al momento trascurabile
            #a ogni iterazione si lavora su un intorno di sk
            markets = copy.deepcopy(sk)
            
            h = random.randint(0, Util.K - 1)
            t0 = random.randint(0, Util.T - 1)
            
            tabumoves = {}
            while (markets[h].x[t0] > 0):
                #f = open("output.txt", "a")
                #f.write(str(markets[h].x[t0]))
                
                t = random.randint(0, Util.T - 1)
                while (t == t0):
                    t = random.randint(0, Util.T - 1)
                
                x = random.randint(1, markets[h].x[t0])
                
                move = Moves(h, t0, t, x)
                #f.write(str(h) + str(t0) + str(t) + str(x))
                #f.write(str(markets[h]))
                #si controlla il valore ritornato dal metodo do (si verifica che la mossa sia fattibile)
                #valutare se dati h e t0 esistono sempre mosse fattibili
                if(markets[h].do(move)):
                    #f.write("Mossa")
                    if(t in tabumoves):
                        tabumoves[t].x = tabumoves[t].x + move.x
                    else:
                        tabumoves[t] = copy.deepcopy(move)
                
                #f.close()
            
            marketscost = Markets.cost(markets)
            
            #lista delle mosse dell'intorno
            neighborhood.append((copy.deepcopy(marketscost), copy.deepcopy(markets), copy.deepcopy(tabumoves)))
            
            #if(i == 0):
            #    bestneighbor = copy.deepcopy(markets)
            #    bestneighbormoves = copy.deepcopy(tabumoves)
            #    bestneighborcost = copy.deepcopy(marketscost)
            
            #if(marketscost < bestneighborcost):
            #    bestneighbor = copy.deepcopy(markets)
            #    bestneighbormoves = copy.deepcopy(tabumoves)
            #    bestneighborcost = copy.deepcopy(marketscost)
                
            i = i + 1
        
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