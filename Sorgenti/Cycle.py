# coding: utf-8


import Util
import copy

#lettura del file e immisione dei dati in un dizionario {id, lista[nodoA,nodoB,costo]}
def readCostFile():
    cost_dictionary={}
    
    fileInput=open(Util.inputCost,"r")
    line = fileInput.readline() #buttiamo via la prima lina di commento
    
    i=0
    while 1:
        line = fileInput.readline()
        if(line==""):
            break
        app = line.split(' ')
        applist=[app[0],app[1],int(app[2])]
        cost_dictionary[i]=applist 
        i=i+1
    
    fileInput.close()
    
    
    return cost_dictionary

#funzione che ritorna il costo di ogni nodo dal dizionario che contiene il costo di tutti i nodi
def ArcCost(nodeA,nodeB,input_dictionary):
    cost=0
    for f in input_dictionary.items():
        if(nodeB<nodeA):
           app=nodeB
           nodeB=nodeA
           nodeA=app
        app=f[1]
        if(app[0]==nodeA and app[1]==nodeB):
                cost= app[2]   
    
    return cost

#funzione che calcola il costo per inserire 2 archi nel grafo e togliere quello comune
def CostCalculate(insertnode,input_dictionary,item_dictionary):
    beastcost=-1
    appcost=0
    indexadd=0
    app_item_dictionary=[]
    app_item_dictionary=copy.deepcopy(item_dictionary)
    input_partial_cycle =app_item_dictionary[1]

    
    for i in range(0, len(input_partial_cycle)-2):
        if (input_partial_cycle[i]!='-'):
            appcost=ArcCost(input_partial_cycle[i], insertnode, input_dictionary)+ArcCost(insertnode, input_partial_cycle[i+2], input_dictionary)-ArcCost(input_partial_cycle[i], input_partial_cycle[i+2], input_dictionary)

            if(appcost<beastcost or beastcost==-1):
                beastcost=appcost
                indexadd=i
    
   
    output_partial_cycle=input_partial_cycle[0:int(indexadd)+1]
    output_partial_cycle=output_partial_cycle+"-"+insertnode
    output_partial_cycle=output_partial_cycle+input_partial_cycle[int(indexadd)+1::]
    app_item_dictionary[0]=app_item_dictionary[0]+beastcost
    app_item_dictionary[1]=output_partial_cycle
    
    return app_item_dictionary


#metodo che crea tutte le possibili conmbinazioni di cicli
def CreateCycles(): 
    separator="-"
    input_dictionary=readCostFile() #lettura del file e memorizzazione degli archi in un dizionario
    cycles_dictionary={}
    output_dictionary={}
    app_dictionary={}
    
    #genero tutti i cicli con 2 nodi
    for i in range (0,Util.K):
        for j in range (0,len(input_dictionary)):
            element_list=input_dictionary[j]
            if(element_list[1]=='z'):
                index=element_list[0]+element_list[1]
                app=[]
                app.append(2*element_list[2])
                app.append(element_list[1]+separator+element_list[0]+separator+element_list[1])
                
                cycles_dictionary[index] = app 
                
    
    output_dictionary=copy.deepcopy(cycles_dictionary)

    
    
    for h in range(0, Util.K-1): 
        #print "h: ", h
        for i in range (0,len (cycles_dictionary)):
            
            index_list=cycles_dictionary.keys()
            app_index=index_list[i]
            final_index=""

            for j in range (ord('a'),ord('a')+Util.K): 
                              
                if (app_index.find(chr(j))==-1):
                    add_element= CostCalculate(chr(j),input_dictionary,cycles_dictionary[index_list[i]])
                    
                    
                    
                    for counter in range (0,len(app_index)):
                        if(app_index[counter]>chr(j)):
                            final_index=app_index[0:counter]
                            final_index=final_index+chr(j)
                            final_index=final_index+app_index[counter::]
                            break
                    
                    
                    if(final_index in(app_dictionary)): 
                        element=app_dictionary[final_index]
                        
                        if(add_element[0]<element[0]):
                            app_dictionary[final_index]=add_element
                    else:
                        app_dictionary[final_index]=add_element                    
                            
            
            output_dictionary.update(app_dictionary) 
        cycles_dictionary=copy.deepcopy(app_dictionary)
                
        app_dictionary={}
    return output_dictionary   
    
