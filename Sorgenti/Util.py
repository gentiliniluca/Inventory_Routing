# coding: utf-8

global K
K=10

global Q
Q = 250

global T
T=5

global ITERATIONS
ITERATIONS = 128

global MAXSTALLCOUNTER
MAXSTALLCOUNTER = 32

global INTENSIFICATION
INTENSIFICATION = 4

global DIVERSIFICATION
DIVERSIFICATION = 4

global N #numero di soluzioni nell'intorno
N = 64

global TABULISTDIM
TABULISTDIM = 20

global inputFile
inputFile="input.txt"

global inputCost
inputCost="distanceCosts.txt"


def subfinder(sublist, list):
    
    find = 0
    for e in sublist:
        if(e in list):
            find = find + 1
    
    if ((len(sublist) - find) == 0):
        return True
    
    return False

