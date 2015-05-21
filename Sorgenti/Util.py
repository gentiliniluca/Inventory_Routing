# coding: utf-8

#from Markets import Markets

global K
K=10

global Q
Q = 300

global T
T=5

global ITERATIONS
ITERATIONS = 100

global N #numero di soluzioni nell'intorno
N = 10

global TABULISTDIM
TABULISTDIM = 15

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

