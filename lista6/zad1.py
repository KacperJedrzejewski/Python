from duze_cyfry import dajCyfre
from turtle import *
tracer(4,0)

n = 5
kolory=['green','red','blue','yellow','black','white','brown','orange','grey','pink']
def kwadrat():
    
    for i in range(4):
        fd(n)
        rt(90)
    


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
        bk(len(liczba)*6*n)
        rt(90)
        fd(n)
        lt(90)
        pd()
        tmp,k=0,1
        fillcolor(kolory[0])
        for j in buff:
            if tmp == 6:
                fillcolor(kolory[k])
                k += 1 
                k = k % 10
                tmp = 0
            tmp += 1
            if j == '#':
                begin_fill()
                kwadrat()
                end_fill()
            else:
                pu()
                kwadrat()
                pd()
            pu()
            fd(n)
            pd()

dlc(12443234243456789)
input()