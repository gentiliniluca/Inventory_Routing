import random

import Util
from Markets import Markets
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
condition = True
while condition:
    # selezionare la miglior soluzione dell'intorno, anche peggiore
    # per il momento selezione casuale
    
    i = 0
    while i < Util.N: #la probabilità di due soluzioni uguali è al momento trascurabile
        #a ogni iterazione si lavora su un intorno di sk
        markets = sk
        
        h = random.randint(0, Util.K - 1)
        t0 = random.randint(0, Util.T - 1)
        
        m = 0
        while (markets[h].x[t0] > 0):
            
            t = random.randint(0, Util.T - 1)
            while (t == t0):
                t = random.randint(0, Util.T - 1)
            
            x = random.randint(1, markets[h].x[t0])
            
            move = Moves(t0, t, x)
            
            markets[h].do(move, load)
            
            if(m == 0):
                tabumove = move
            else:
                if(tabumove.t == move.t):
                    tabumove.x = tabumove.x + move.x
                else:
                    tabumove.t0 = None
            m = m + 1
            
        if(i == 0):
            bestneighbor = markets
          
        if(Util.cost(markets) < Util.cost(bestneighbor)):
            bestneighbor = markets
    
    if(Util.cost(bestneighbor) < Util.cost(bestsolution)):
        bestsolution = bestneighbor
    else:
        if(tabumove in tabulist):
            continue
        else:
            sk = bestneighbor
            if(tabumove.t0 != None):
                tabulist.append(Move(tabumove.t, tabumove.t0, tabumove.x))
                if(len(tabulist) > Util.TABULISTDIM):
                    tabulist.pop(0)
    k = k + 1
    #condition = false