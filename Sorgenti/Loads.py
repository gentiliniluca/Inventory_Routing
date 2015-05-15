from Markets import Markets

class Loads:
    
    values = []
    
    def __init__(self, markets):
        
        value = 0
        for t in range(len(markets.x)):
            for h in range(len(markets)):
                value = value + markets[h].x[t]
            self.values.append(value)