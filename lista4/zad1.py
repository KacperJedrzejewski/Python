# rekurencja od 2 do 18 
# rysuj kwadrat jak skonczysz to rt(90)
from turtle import *

speed("fastest")
def mieszanina(k1, k2, a):
  r1,g1,b1 = k1
  r2,g2,b2 = k2
  
  r3 = (1-a) * r1 + a * r2
  g3 = (1-a) * g1 + a * g2
  b3 = (1-a) * b1 + a * b2	
  
  return (r3,g3,b3)


def kwadrat(dlugosc):
	for i in range(4):
		fd(dlugosc)
		lt(90)



def linia(ile,dlugosc,kolor):
	fillcolor(kolor)
	begin_fill()
	if ile == 2:
		kwadrat(dlugosc)
		fd(dlugosc)
	else:	
		for i in range(ile-2):
			kwadrat(dlugosc)
			fd(dlugosc)
	kwadrat(dlugosc)		 	
	rt(90)
	end_fill()


for i in range(2,20):

	a = i / 30
	linia(i,25,mieszanina((1,1,0),(1,0,1),a))	
input()