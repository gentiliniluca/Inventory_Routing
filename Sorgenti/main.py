import random

import Util
from Markets import Markets
from Moves import Moves
from Loads import Loads

#reperire i dati iniziali (da un qualcosa)


# inizializzare il problema con una soluzione banale
markets = []
for h in range(Util.K):
    markets.append(Markets(S[h], S1[h], q[h]))
    
load = Loads(markets)

#come soluzione si intende la situazione dei supermercati
bestsolution = markets
sk = markets
#ciclo contenente l'algoritmo
k = 1
tabulist = []
while k < 1000:
    # selezionare la miglior soluzione dell'intorno, anche peggiore
    # per il momento selezione casuale
    
    i = 0
    while i < Util.N: #la probabilità di due soluzioni uguali è al momento trascurabile
        #a ogni iterazione si lavora su un intorno di sk
        markets = sk
        
        h = random.randint(0, Util.K - 1)
        t0 = random.randint(0, Util.T - 1)
        
        tabumoves = []
        periods = {}
        while (markets[h].x[t0] > 0):
            
            t = random.randint(0, Util.T - 1)
            while (t == t0):
                t = random.randint(0, Util.T - 1)
            
            x = random.randint(1, markets[h].x[t0])
            
            move = Moves(h, t0, t, x)
            
            markets[h].do(move, load)
            
            if(t in periods):
                tabumoves[t].x = tabumoves[t].x + move.x
            else:
                periods[t] = True
                tabumoves.append(move)
            
        if(i == 0):
            bestneighbor = markets
            bestneighbormoves = tabumoves
          
        if(Util.cost(markets) < Util.cost(bestneighbor)):
            bestneighbor = markets
            bestneighbormoves = tabumoves  
    
    if(Util.cost(bestneighbor) < Util.cost(bestsolution)):
        bestsolution = bestneighbor
    else:   
        if(bestneighbormoves in tabulist):
            continue
        else:
            sk = bestneighbor
            tabulist.extend(bestneighbormoves)
            while(len(tabulist) > Util.TABULISTDIM):
                tabulist.pop(0)
    k = k + 1