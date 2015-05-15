from Markets import Markets
from Loads import Loads

#reperire i dati iniziali (da un qualcosa)


# inizializzare il problema con una soluzione banale
markets = []
for h in range(K):
    markets.append(Markets(S[h], S1[h], q[h]))
    
load = Loads(markets)

#ciclo contenente l'algoritmo
condition = True
while condition:
    