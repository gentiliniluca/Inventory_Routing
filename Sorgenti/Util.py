# coding: utf-8

#from Markets import Markets

global K
K=4

global Q

global T
T=5

global N #numero di soluzioni nell'intorno

global TABULISTDIM

global inputFile
inputFile="input.txt"



def subfinder(sublist, list):
    
    find = 0
    for e in sublist:
        if(e in list):
            find = find + 1
    
    if ((len(sublist) - find) == 0):
        return True
    
    return False

