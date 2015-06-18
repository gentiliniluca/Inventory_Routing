# coding: utf-8

import random
import copy
import itertools
from operator import itemgetter
import time

import Util
import File
import Cycle
from Markets import Markets
from Moves import Moves
import Neighborhood


start = time.time()
#reperimento dei dati iniziali dal file di input e inizializzazione del problema con una soluzione banale
markets = []
markets = File.readFile()
cycles_dictionary=Cycle.CreateCycles()
#for h in range(Util.K):
#    markets.append(Markets(S[h], S1[h], q[h]))
#    
#load = Loads(markets)

#come soluzione si intende la situazione dei supermercati
bestsolution = copy.deepcopy(markets)
bestsolutioncost = Markets.cost(bestsolution,cycles_dictionary)
print "\t\t\t\tBest solution cost: ", bestsolutioncost

sk = copy.deepcopy(markets)
sk = Markets.updateWeights(sk)
#ciclo contenente l'algoritmo
tabulist = []
newneighborhood = True
k = 0
stallcounter = 0
intensification = 0
diversification = 0
#print "\nExecution:  " + "\t",
tmp = -1
while ((k < Util.ITERATIONS) and (stallcounter < Util.MAXSTALLCOUNTER)):
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
    skcost = Markets.cost(sk,cycles_dictionary)
    #bestsolutioncost = Markets.cost(bestsolution)
    #print "i & d ", intensification, diversification
    weights = Markets.getWeights(sk)
    if(intensification >= Util.INTENSIFICATION):
        # Per l'intensificazione si cerca di rifornire quelli che si riforniscono più spesso
        # Si selezionano quindi quelli riforniti di meno
        weights = sorted(weights, key = itemgetter(2), reverse=True)
        weights = sorted(weights, key = itemgetter(0))
        #print "intensification: ", weights
        print "Intensification!"
        
        i = 0
        w, h, t0 = weights[i]
        while(len(neighborhood) == 0):
            
            if(sk[h].x[t0] > 0):
                #print h, t0
                returned = Neighborhood.new(neighborhood, bestsolution, bestsolutioncost, sk, skcost, h, t0, tabulist, cycles_dictionary)
            
            i = i + 1
            w, h, t0 = weights[i]
        
        #intensification = 0
    else:
        if(diversification >= Util.DIVERSIFICATION):
            weights = sorted(weights, key = itemgetter(2), reverse=True)
            weights = sorted(weights, key = itemgetter(0), reverse=True)
            #print "diversifcation: ", weights
            print "Diversifcation!"            
            
            i = 0
            w, h, t0 = weights[i]
            while(len(neighborhood) == 0):
            
                if(sk[h].x[t0] > 0):
                    returned = Neighborhood.new(neighborhood, bestsolution, bestsolutioncost, sk, skcost, h, t0, tabulist, cycles_dictionary)
                
                i = i + 1
                w, h, t0 = weights[i]
            
            #diversification = 0
        else:
            for h in range(0, Util.K):
                
                for t0 in range(0, Util.T):
                    #print sk[h].x[t0]
                    
                    returned = "allneighbors"
                    if(sk[h].x[t0] > 0):
                        returned = Neighborhood.new(neighborhood, bestsolution, bestsolutioncost, sk, skcost, h, t0, tabulist, cycles_dictionary)
                    
                    if(returned != "allneighbors"):
                        break
                if(returned != "allneighbors"):
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
    sk = Markets.updateWeights(sk)
    #print bestsolutioncost, bestneighborcost
    if(returned == "bestsolution"):
        bestsolution = copy.deepcopy(bestneighbor)
        bestsolutioncost = copy.deepcopy(bestneighborcost)
        
        intensification = intensification + 1
        diversification = 0
    else:
        diversification = diversification + 1
        intensification = 0
    
    if(intensification >= 2*Util.INTENSIFICATION):
        intensification = 0
    if(diversification >= 2*Util.DIVERSIFICATION):
        diversification = 0
        
    tabulist.append(bestneighbormove)
    while(len(tabulist) > Util.TABULISTDIM):
        tabulist.pop(0)

    if(returned == "bestsolution"):
        stallcounter = 0
    else:
        stallcounter = stallcounter + 1
    
    print "Best neighbor cost: ", bestneighborcost, "\tBest solution cost: ", bestsolutioncost 
      
    k = k + 1
#print " - 100%\n"
print "\nTempo di esecuzione:", int(time.time()-start), "seconds\n\nLa soluzione migliore e':\n"

for h in bestsolution:
    print h.toString()
print ""
index="z"  
for i in range(Util.T):
    for j in range (Util.K):
        if(bestsolution[j].x[i]>0):
            for counter in range (0,len(index)):
                if(index[counter]>chr(j+97)):
                    app_index=index[0:counter]
                    app_index=app_index+chr(j+97)
                    app_index=app_index+index[counter::]
                    index=app_index
                    break
    print "Periodo T =",i+1,"\tOrdine di visita dei nodi: ",cycles_dictionary[index][1],"\tCosto: ", cycles_dictionary[index][0]," km"
    index="z"            
print "\nCosto: " + str(bestsolutioncost)+" km"
#f.write("Cost:" + str(bestsolutioncost))

#f.close()