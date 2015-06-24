import copy

from Markets import Markets
from Moves import Moves
import Util

def new(neighborhood, bestsolution, bestsolutioncost, sk, skcost, h, t0, tabulist, cycles_dictionary, penality):
        
    t1 = sk[h].x[t0]
    
    while(t1 >= 0):
        
        t2 = sk[h].x[t0] - t1
        
        while(t2 >= 0):
            
            t3 = sk[h].x[t0] - t1 - t2
            
            while(t3 >= 0):
                
                t4 = sk[h].x[t0] - t1 - t2 - t3
                
                x = [t1, t2, t3, t4]
                    
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
                    marketscost, exceeded = Markets.cost(markets, cycles_dictionary, penality)
                    #print marketscost, skcost, bestsolutioncost
                    if(marketscost < bestsolutioncost):
                        bestsolution = copy.deepcopy(markets)
                        neighborhood.append((marketscost, markets, (h, t0)))
                        return "bestsolution"
                    else:
                        if(not tabumove):
                            neighborhood.append((copy.deepcopy(marketscost), copy.deepcopy(markets), (h, t0)))
                            if(marketscost < skcost):
                                return "betterneighbor"
                            
                domove = True
                tabumove = False
                
                t3 = t3 - 1
            t2 = t2 - 1
        t1 = t1 - 1
    return "allneighbors"
    