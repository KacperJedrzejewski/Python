from math import sqrt

def ile(tab):
	ile = 0
	for i in range(6,10):
		if tab[i] != 7: 
			tab[i] = 0
			for j in range(10):
				tab[i % 10] = j
				if pierwsza(tab):
					ile += 1
				for j1 in range(10):
					tab[(i + 1 ) % 10] = j1
					if pierwsza(tab):
						ile += 1
					for j2 in range(10):
						tab[(i + 2) % 10] = j2
						if pierwsza(tab):
							ile += 1
			return ile
 
def pierwsza(tablica):
	tmp = ''
	for i in range(10):
		tmp += str(tablica[i])
	for i in range(2,int(sqrt(int(tmp)))):
 		if int(tmp) % i == 0: 
 			return False
	return True

def krok(tablica):
	tmp = 0	
	for i in range(3):
		tmp += ile(tablica)
		#print(tablica)
		tablica[i] = 0
		tablica[i + 7] = 7  
	return tmp


tablica = []
tablica += (7,7,7,7,7,7,7,0,0,0)
print(krok(tablica))