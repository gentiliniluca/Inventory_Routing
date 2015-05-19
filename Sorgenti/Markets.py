# coding: utf-8

import Util
from Moves import Moves

class Markets:
    SMax = None
    S = []
    q = []
    x = []
    w = []
    
    #inizializza il supermercato con una soluzione iniziale
    def __init__(self, Sh, Sh1, q):
        
        self.SMax = Sh
        self.S = [Sh] * Util.T
        self.q = q
        self.x = q
        self.w = [0] * Util.T
    
    #I vincoli mantenuti sono:
    #Sht+1 = Sht - qht + xht
    #Sh1 = ShT
    #SMax >= Sht
    #Somma xht = Somma qht
    def do(self, move):
        
        if (move.t0 < move.t):
            for t in range(move.t + 1, move.t0 + 1):
                if(self.S[t] - move.x < 0): #se la mossa rende negative le scorte
                    return False
        else:
            for t in range(move.t + 1, move.t0 + 1):
                if(self.S[t] + move.x > self.SMax): #se la mossa supera la capacità del magazzino
                    return False
        
        if (move.t0 < move.t):
            for t in range(move.t0 + 1, move.t + 1):
                self.S[t] = self.S[t] - move.x
        else:
            for t in range(move.t + 1, move.t0 + 1):
                self.S[t] = self.S[t] + move.x
        
        return True

    def toString(self):
    	stringa = "Capacita' max= ", self.SMax, " Scorte iniziali= ", self.S, " Consumo[] ", self.q
    	return stringa
