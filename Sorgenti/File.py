# coding: utf-8

import Util
from Markets import Markets


def readFile():  
    try:
        markets = []
        in_file = open(Util.inputFile,"r")
        line = in_file.readline()   #prima linea inutile che rappresenta il commento
        ct = 0
        while ct < Util.K:
            line = in_file.readline()
            #print line
            a = line.split(' ')
            m = Markets(int(a[1]), int(a[2]), map(int, a[3:(int(Util.T)+3)]))  #mi creo l'oggetto market
            markets.append(m)              #appendo alla lista
            ct += 1
        in_file.close()
    
    except Exception as e:
        print e
    
    finally:
        return markets