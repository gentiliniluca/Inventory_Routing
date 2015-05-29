# coding: utf-8

import random
import copy
import itertools
from operator import itemgetter
import time

import Util
import File
from Markets import Markets
from Moves import Moves
from itertools import permutations

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
#print "\nExecution:  " + "\t",
tmp = -1
while k < Util.ITERATIONS:
    #f = open("output.txt", "a")
    #f.write("K =" + str(k))
    #f.close()
    #print k
    
    
    
    #Un po' di piacere per gli occhi...
    #perCent = k*100//Util.ITERATIONS
    #if(perCent % 10 == 0 and tmp != perCent):
    #    if(tmp != -1):
    #        print " - ",
    #    print str(perCent) + "%",
    #    tmp = perCent
    
    
    # selezionare la miglior soluzione dell'intorno, anche peggiore
    # per il momento selezione casuale
    
    #verificare se è necessario lavorare in un nuovo vicinato (lettura del parametro impostato sotto) e che il vicinato attuale contenga almeno un elemento 
    neighborhood = []
    firstimprovement = False
    skcost = Markets.cost(sk)
    h = 0
    for h in range(0, Util.K):
        t0 = 0
        for t0 in range(0, Util.T):
            print sk[h].x[t0]
            if(sk[h].x[t0] > 0):
                t1 = sk[h].x[t0]
                t2 = 0
                while(t1 >= t2):
                    t2 = sk[h].x[t0] - t1
                    t3 = 0
                    while(t2 >= t3):
                        t3 = sk[h].x[t0] - t1 - t2
                        t4 = 0
                        while(t3 >= t4):
                            t4 = sk[h].x[t0] - t1 - t2 - t3
                            if((t1>=t2) and (t2>=t3) and (t3>=t4)):
                                # trovata una mossa valida
                                permutations = []
                                for l in list(itertools.permutations((t1, t2, t3, t4))):
                                    if(not l in permutations):
                                        permutations.append(l)
                                #trovate tutte le permutazioni
                                
                                for p in permutations:
                                    x = []
                                    for e in p:
                                        x.append(e)
                                        
                                    markets = copy.deepcopy(sk)
                                    
                                    i = 0
                                    t = 0
                                    domove = True
                                    tabumove = False
                                    for t in range(0, Util.T):
                                        
                                        if(t != t0):
                                            if(x[i] > 0):
                                                move = Moves(h, t0, t, x[i])
                                                if(markets[h].do(move)):
                                                    if((h, t) in tabulist):
                                                        tabumove = True
                                                else:
                                                    domove = False
                                                #print "move", h, t0, t, x[i], domove, tabumove
                                            i = i + 1
                                    
                                    
                                    if(domove):
                                        marketscost = Markets.cost(markets)
                                        print marketscost, skcost, bestsolutioncost
                                        if(marketscost < bestsolutioncost):
                                            firstimprovement = True
                                            bestsolution = copy.deepcopy(markets)
                                            bestsolutioncost = copy.deepcopy(marketscost)
                                            neighborhood.append((bestsolutioncost, bestsolution, (h, t0)))
                                        else:
                                            if(not tabumove):
                                                neighborhood.append((copy.deepcopy(marketscost), copy.deepcopy(markets), (h, t0)))
                                                if(marketscost < skcost):
                                                    firstimprovement = True
                                                
                                    domove = True
                                    tabumove = False
                                        
                                    if(firstimprovement):
                                        break
                            t3 = t3 - 1
                            if(firstimprovement):
                                break
                        t3 = 0
                        t2 = t2 - 1
                        if(firstimprovement):
                            break
                    t2 = 0
                    t1 = t1 - 1
                    if(firstimprovement):
                        break
            if(firstimprovement):
                break
        if(firstimprovement):
            break
        
    #ordinare per costo crescente la lista e prendere il primo elemento (migliore)
    neighborhood = sorted(neighborhood, key = itemgetter(0))
    bestneighborcost, bestneighbor, bestneighbormove = neighborhood[0]
    
    #if(bestneighborcost < bestsolutioncost):
    #    bestsolution = copy.deepcopy(bestneighbor)
    #    bestsolutioncost = copy.deepcopy(bestneighborcost)
    #else:
    #    if(Util.subfinder(bestneighbormoveslist, tabulist)):
    #        newneighborhood = False
    #        neighborhood.pop(0)
    #        continue
    
    #newneighborhood = True       
    sk = copy.deepcopy(bestneighbor)
    tabulist.append(bestneighbormove)
    while(len(tabulist) > Util.TABULISTDIM):
        tabulist.pop(0)    
    k = k + 1
#print " - 100%\n"
print "Elapsed time:", int(time.time()-start), "seconds\n\nThe best solution is:"

for h in bestsolution:
    print h.toString()
    
print "\nCost: " + str(bestsolutioncost)
#f.write("Cost:" + str(bestsolutioncost))

#f.close()