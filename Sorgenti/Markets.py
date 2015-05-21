# coding: utf-8

import copy

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
        self.S = [Sh1] * Util.T
        self.q = copy.deepcopy(q)
        self.x = copy.deepcopy(q)
        self.w = [0] * Util.T
        #utilizzare il peso ù.ù
    
    #I vincoli mantenuti sono:
    #Sht+1 = Sht - qht + xht
    #Sh1 = ShT
    #SMax >= Sht
    #Somma xht = Somma qht
    def do(self, move):
        
        if (move.t0 < move.t):
            for t in range(move.t0 + 1, move.t + 1):
                if(self.S[t] - move.x < 0): #se la mossa rende negative le scorte
                    return False
        else:
            for t in range(move.t + 1, move.t0 + 1):
                if(self.S[t] + move.x > self.SMax): #se la mossa supera la capacità del magazzino
                    return False
        
        self.x[move.t0] = self.x[move.t0] - move.x
        self.x[move.t] = self.x[move.t] + move.x 
        
        if (move.t0 < move.t):
            for t in range(move.t0 + 1, move.t + 1):
                self.S[t] = self.S[t] - move.x
            
        else:
            for t in range(move.t + 1, move.t0 + 1):
                self.S[t] = self.S[t] + move.x
          
        return True
      
    def toString(self):
    	stringa = "Capacita' max= ", self.SMax, " Scorte = ", self.S, " Consumo= ", self.q, "Rifornimento= ", self.x
    	return stringa
 
 
 
    @staticmethod
    def cost(markets):
        cost = 0    
        
        for t in range(Util.T):
            value = 0 #variabile che tiene conto del carico sul camion nel singolo periodo t
            for h in range(Util.K):
                if(markets[h].x[t] > 0): #se porto materiale al market allora incremento il costo perchè faccio un giro
                    cost = cost + 1
                    value = value + markets[h].x[t]
            if(value > Util.Q): #controllo se supero la capacità del camion, se si aumento il costo
                cost = cost + 2
                #calcolo del costo: variabile furgone incrementata di 1 ogni volta che si sfora la capacità
                #poi costo = costo*(1+furgone/2T)
                 
        return cost