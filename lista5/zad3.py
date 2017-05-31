L1 = sorted([5,4,3,1,2,6])
L2 =[5,3,1,4,6,4,9]
def Sortowanie(lista):
	dlugosc = len(lista)
	lista1= lista
	lista1.sort()
	tmp = [[]]
	tmp[0] = lista1[0]
	j=0
	for i in range(1,dlugosc):
		if lista[i-1] != lista[i]:
			j += 1
			tmp += [lista[i]]
	
	return tmp
A = list(range(100000000))
#A = [6,53,5,1,3,4,2,2,2,2,2,2,2,2,2,4,4,4,3,3,44,34,234,2]
print(len(Sortowanie(A)))