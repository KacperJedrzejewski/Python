import random

def randperm(n):
	tmp = []
	wynik = []
	for i in range(n):
		tmp.append(i)
	for i in range(n):
		tmp1 = random.choice(tmp)
		wynik.append(tmp1)
		tmp.remove(tmp1)

	return wynik

for i in range(4):
	print(randperm(10))