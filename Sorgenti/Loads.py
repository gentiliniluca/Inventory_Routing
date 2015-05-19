# coding: utf-8

import Util
from Markets import Markets
from Moves import Moves

class Loads:
    
    values = []
    
    def __init__(self, markets):
        
        value = 0
        for t in range(Util.T):
            for h in range(Util.K):
                value = value + markets[h].x[t]
            self.values.append(value)
            
    def do(self, move):
        self.values[move.t0] = self.values[move.t0] - move.x
        self.values[move.t] = self.values[move.t] + move.x