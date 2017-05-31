from duze_cyfry import dajCyfre
from turtle import *
tracer(4,0)

n = 20
def dlc(liczba):
    liczba = str(liczba)
    liczbaTable = []

    for i in range(len(liczba)):
        liczbaTable += [dajCyfre(int(liczba[i]))]
    
    lineTable = [[] for x in range(5)]
     

    for i in range(len(liczbaTable)):
        for j in range(len(liczbaTable[i])):
            lineTable[j] += [liczbaTable[i][j]]
    
    for i in range(len(lineTable)):
        buff = ""
        for j in range(len(lineTable[i])):
            buff += " " + lineTable[i][j]
        
        pu()
        bk(5*n)
        rt(90)
        fd(n)
        lt(90)
        pd()
        for j in buff:
            if j == '#':
                kwadrat()
            else:
                pu()
                kwadrat()
                pd()
            pu()
            fd(n)
            pd()

dlc(1234)
