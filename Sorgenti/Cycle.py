# coding: utf-8


import Util
import copy


def readCostFile():
    costDictionary={}
    
    fileInput=open(Util.inputCost,"r")
    line = fileInput.readline() #buttiamo via la prima lina di commento
    
    i=0
    while 1:
        line = fileInput.readline()
        if(line==""):
            break
        app = line.split(' ')
        applist=[app[0],app[1],int(app[2])]
        costDictionary[i]=applist 
        i=i+1
    
    fileInput.close()
    
    
    return costDictionary

def ArcCost(nodeA,nodeB,inputDictionary):
    cost=0
    for f in inputDictionary.items():
        if(nodeB<nodeA):
           app=nodeB
           nodeB=nodeA
           nodeA=app
        app=f[1]
        if(app[0]==nodeA and app[1]==nodeB):
                cost= app[2]   
    
    return cost

def CostCalculate(insertnode,inputDictionary,itemDictionary):
    beastcost=-1
    appcost=0
    indexadd=0
    appItemDctionary=[]
    appItemDctionary=copy.deepcopy(itemDictionary)
    inputPartialCycle =appItemDctionary[1]
    for i in range(0, len(inputPartialCycle)-2):
        if (inputPartialCycle[i]!='-'):
            appcost=ArcCost(inputPartialCycle[i], insertnode, inputDictionary)+ArcCost(insertnode, inputPartialCycle[i+2], inputDictionary)-ArcCost(inputPartialCycle[i], inputPartialCycle[i+2], inputDictionary)
            if(appcost<beastcost or beastcost==-1):
                beastcost=appcost
                indexadd=i
    
    #print appItemDctionary
    outputPartialCycle=inputPartialCycle[0:int(indexadd)+1]
    outputPartialCycle=outputPartialCycle+"-"+insertnode
    outputPartialCycle=outputPartialCycle+inputPartialCycle[int(indexadd)+1::]
    appItemDctionary[0]=appItemDctionary[0]+beastcost
    appItemDctionary[1]=outputPartialCycle
    #print appItemDctionary
    return appItemDctionary



def CreateCycles():
    separator="-"
    inputDictionary=readCostFile()
    CyclesDictionary2={}
    
    
    for i in range (0,4): #da mettere Util.K
        for j in range (0,len(inputDictionary)):
            elementList=inputDictionary[j]
            if(elementList[1]=='z'):
                index=elementList[0]+elementList[1]
                app=[]
                app.append(2*elementList[2])
                app.append(elementList[1]+separator+elementList[0]+separator+elementList[1])
                
                CyclesDictionary2[index] = app 
                
    
    
    for i in range (0,len (CyclesDictionary2)):
        indexList=CyclesDictionary2.keys()
        app=indexList[i]
        finalindex=""
        for j in range (ord('a'),ord('a')+4): #al posto di 4 ci va Util.K
            if (app.find(chr(j))==-1):
                addElement= CostCalculate(chr(j),inputDictionary,CyclesDictionary2[indexList[i]])
                
                for counter in range (0,len(app)):
                    if(app[counter]>chr(j)):
                        finalindex=app[0:counter]
                        finalindex=finalindex+chr(j)
                        finalindex=finalindex+app[counter::]
                        break
                
                
                print finalindex
                print addElement
                
                if(finalindex in(CyclesDictionary2)): 
                    print "Entrato",finalindex
                    element=CyclesDictionary2[finalindex]
                    if(addElement[0]<element[0]):
                        CyclesDictionary2[finalindex]=addElement
                else:
                    CyclesDictionary2[finalindex]=addElement                    
                        
             
                    
    print CyclesDictionary2

CreateCycles()
