# coding: utf-8


import Util


def readCostFile():
    costDictionary={}
    
    fileInput=open(Util.inputCost,"r")
    line = fileInput.readline() #buttiamo via la prima lina di commento
    
    while 1:
        line = fileInput.readline()
        if(line==""):
            break
        app = line.split(' ')
        costDictionary[app[0]]=int(app[1])
    
    fileInput.close()
    
    return costDictionary
    

def CreateCycles():
    inputDictionary=readCostFile()
    CyclesDictionary={}
    
    letter='z'
    for f in inputDictionary.items():
        arc , cost=f
        
        if(arc.startswith(letter)):
            CyclesDictionary[arc]=int(cost)
            
                 
    print CyclesDictionary


CreateCycles()
