import random
from turtle import *

#speed("fastest")
def drzewo(dlugosc):
    if dlugosc > 14 :
       fd(dlugosc)
       kat = random.randint(10,35)
       lewe(dlugosc*0.8, kat)
       prawe(dlugosc*0.8, kat)

def lewe(dlugosc,kat):
    kat1 = random.randint(10,35)
    if dlugosc > 14 :
      lt(kat)
      fd(dlugosc) 
      lewe(dlugosc*0.8, kat1)
      prawe(dlugosc*0.8, kat1)
      bk(dlugosc)
      rt(kat)

def prawe(dlugosc,kat): 
    kat1 = random.randint(10,35)
    if dlugosc > 14:
       rt(kat)
       fd(dlugosc)
       lewe(dlugosc*0.8, kat1)
       prawe(dlugosc*0.8, kat1)
       bk(dlugosc)
       lt(kat)

rt(90)
pu()
fd(100)
pd()
lt(180)
drzewo(100)
input()