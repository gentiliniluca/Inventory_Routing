from Moves import Moves

class Markets:
    SMax = None
    S = []
    q = []
    x = []
    w = []
    
    #inizializza il supermercato con una soluzione iniziale
    def __init__(self, Sh, Sh1, q):
        self.T = len(q)
        
        self.SMax = Sh
        self.S = [Sh] * self.T
        self.q = q
        self.x = q
        self.w = [0] * self.T
        
    def constraints(self, move):
        
        if (move.t0 > move.t):
            for t in range(t0+1, t+1):
                if(self.S[t] > self.SMax):
                    return False
        
        return True
    
    #update bilancio ai nodi