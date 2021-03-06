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
    	stringa = "Capacità max = " + str(self.SMax) + "\tScorte = " + str(self.S) + "\tConsumo = " + str(self.q) + "\tRifornimento = " + str(self.x)
    	return stringa
 
 
 
    @staticmethod
    def cost(markets,cycles_dictionary,penality):
        cost = 0    
        excessloadcamion = 0
        c = 0
        
        index="z" #indice del dizionario dei cicli fatto dai nodi presenti nel ciclio in ordine alfabetico
        
        for t in range(Util.T):
            value = 0 #variabile che tiene conto del carico sul camion nel singolo periodo t
            index="z"
            for h in range(Util.K):
                if(markets[h].x[t] > 0): #se porto materiale al market allora incremento il costo perchè faccio un giro
                    value = value + markets[h].x[t]#carico del camion
                    index=index+chr(h+97)#creo l'indice
            
            index=''.join(sorted(index))
            #print index 
            if(index!="z"):
                cost=cost+cycles_dictionary[index][0] #calcolo del costo complessivo prelevando dall'item del dizionario il costo del ciclo
                
            if(value>Util.Q): #sforo la capacita del camion
                excessloadcamion = excessloadcamion + value - Util.Q
                #calcolo del costo
        
        c=float(excessloadcamion)*(pow(2,penality))
              
        return ((cost*(1 + c)), c)
    
    @staticmethod
    def updateWeights(markets):
        for h in range(Util.K):
            for t in range(Util.T):
                if(markets[h].x[t] > 0):
                    markets[h].w[t] = markets[h].w[t] + 1
        return markets
    
    @staticmethod
    def getWeights(markets):
        weights = []
        for h in range(Util.K):
            for t in range(Util.T):
                weights.append((markets[h].w[t], h, t))
        return weights
        
