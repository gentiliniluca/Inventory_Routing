class Markets:
    SMax = None
    S = []
    q = []
    x = []
    w = []
    
    def __init__(self, Sh, Sh1, q):
        self.SMax = Sh
        self.S.append(Sh1)
        self.q = q
        self.w = [0] * len(q)
        
    
    