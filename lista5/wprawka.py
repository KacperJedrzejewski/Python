from turtle import *
speed('fastest')

def wzorek(n,n1):
	kolory = ['red','orange','green','blue']
	for i in range(36):
		fillcolor(kolory[i%4])
		begin_fill()
		kwadrat(n,n1)
		rt(90)
		fd(n)
		lt(80)
		#rt(10)	
		n1 += 5
		end_fill()
	kolo()


def kwadrat(n,n1):
	for i in range(2):
		fd(n1)
		rt(90)
		fd(n)
		rt(90)

def kolo():
	rt(90)
	fillcolor('yellow')
	begin_fill()
	for i in range(36):
		fd(20)
		rt(10)
	end_fill()


pu()
lt(90)
fd(100)
pd()
wzorek(20,20)
input()