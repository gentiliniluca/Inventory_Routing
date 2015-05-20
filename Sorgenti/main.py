# coding: utf-8

import random
import copy

import Util
from Markets import Markets
from Moves import Moves

#reperimento dei dati iniziali dal file di input e inizializzazione del problema con una soluzione banale
markets = []
markets = Util.readFile()
#for h in range(Util.K):
#    markets.append(Markets(S[h], S1[h], q[h]))
#    
#load = Loads(markets)

#come soluzione si intende la situazione dei supermercati
bestsolution = copy.deepcopy(markets)
bestsolutioncost = Util.cost(bestsolution)
sk = copy.deepcopy(markets)
#ciclo contenente l'algoritmo
k = 0
tabulist = []
while k < 1000:
    # selezionare la miglior soluzione dell'intorno, anche peggiore
    # per il momento selezione casuale
    
    i = 0
    while i < Util.N: #la probabilità di due soluzioni uguali è al momento trascurabile
        #a ogni iterazione si lavora su un intorno di sk
        markets = copy.deepcopy(sk)
        
        h = random.randint(0, Util.K - 1)
        t0 = random.randint(0, Util.T - 1)
        
        tabumoves = {}
        while (markets[h].x[t0] > 0):
            
            t = random.randint(0, Util.T - 1)
            while (t == t0):
                t = random.randint(0, Util.T - 1)
            
            x = random.randint(1, markets[h].x[t0])
            
            move = Moves(h, t0, t, x)
            
            #si controlla il valore ritornato dal metodo do (si verifica che la mossa sia fattibile)
            #valutare se dati h e t0 esistono sempre mosse fattibili
            if(markets[h].do(move)):
            
                if(t in tabumoves):
                    tabumoves[t].x = tabumoves[t].x + move.x
                else:
                    tabumoves[t] = copy.deepcopy(move)
        
        marketscost = Util.cost(markets)
        
        if(i == 0):
            bestneighbor = copy.deepcopy(markets)
            bestneighbormoves = copy.deepcopy(tabumoves)
            bestneighborcost = copy.deepcopy(marketscost)
        
        if(marketscost < bestneighborcost):
            bestneighbor = copy.deepcopy(markets)
            bestneighbormoves = copy.deepcopy(tabumoves)
            bestneighborcost = copy.deepcopy(marketscost)
            
        i = i + 1
    
    if(bestneighborcost < bestsolutioncost):
        bestsolution = copy.deepcopy(bestneighbor)
        bestsolutioncost = copy.deepcopy(bestneighborcost)
    else:
        bestneighbormoveslist = []
        for m in bestneighbormoves:
              bestneighbormoveslist.append(m)
        
        if(Util.subfinder(bestneighbormoveslist, tabulist)):
            continue
        else:        
            sk = copy.deepcopy(bestneighbor)
            tabulist.extend(bestneighbormoveslist)
            while(len(tabulist) > Util.TABULISTDIM):
                tabulist.pop(0)
    k = k + 1