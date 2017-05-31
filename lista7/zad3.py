from turtle import * 

def kwadrat(n,kolor):
	colorfill(kolor)
	begin_fill()
	for i in range(4):
		fd(n)
		rt(90)
	end_fill()



kolory = open('krowiaglowa.txt').read().split()
for i in kolory:
	print(i)

