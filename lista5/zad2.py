from turtle import *
from math import fabs
import random
tracer(4,0)
def kwadrat(n,kolor):
	fillcolor(kolor)
	begin_fill()
	for i in range(4):
		fd(n)
		rt(90)
	end_fill()



for i in range(1000):
	n = random.randint(20,50)
	x = random.randint(-300,300)
	y = random.randint(-300,300)
	k1=random.uniform(0.0,0.15)
	k2=random.uniform(0.0,0.15)
	k3=random.uniform(0.0,0.15)
	if fabs(x) > fabs(y) :
		kolor = (fabs(fabs((x/300))-k1),fabs(fabs((x/300))-k2),fabs(fabs((x/300))-k3))
	else:
		kolor = (fabs(fabs((y/300))-k1),fabs(fabs((y/300))-k2),fabs(fabs((y/300))-k3))  
	pu()
	goto(x,y)
	pd()
	kwadrat(n,kolor)
input()