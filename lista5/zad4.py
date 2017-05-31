from turtle import *

speed('fastest')

BOK = 20

def kwadrat(bok):
  begin_fill()
  for i in range(4):
    fd(bok)
    rt(90)
  end_fill()  

def zlicz(znak, napis):
  licznik = 0
  for z in napis:
    if z == znak:
      licznik += 1
  return licznik
    
def murek(napis):
  N = zlicz('f', napis)
  pozycja = 0
  kolory = ('green','blue','orange','yellow','brown','red')
  for x in napis:
    if x == 'f':
      a = pozycja / N
      kwadrat(BOK)
      pozycja += 1
      fd(BOK)
    elif x == 'r':
      rt(90)
      fd(BOK)
    elif x == 'l':
      bk(BOK)
      lt(90) 
    elif x == 'u':
    	pu()
    elif x == 'd':
    	pd()
    elif x == 'b':
    	bk(BOK) 
    else:

    	fillcolor(kolory[int(x)])
  
murek("0" + 10 * "f" + "r" + "1" + 10* "f" + "r"+ "3" + 10* "f" + "r"+ "4" + 10* "f" + "r")
  
x = input()