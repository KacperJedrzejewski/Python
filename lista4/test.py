 
from math import sqrt
 
#tworzy tablice z wartosciami od "od" (wlacznie) do "do" (wlacznie)
def od_do(od, do):
	zw=[]
	while od!=do+1:
		zw.append(od)
		od+=1
	return zw
 
#sito Eratostenesa dla liczb od 1 do "do"
def sito(do):
	sq = int(sqrt(do)) #gorny zakres dzialania algorytmu
	obecnie=1          #wartosc poczatkowa
	tab=od_do(1, do)   #utworz tablice z wartosciami od 1 do "do"
	while True:
		if obecnie>sq: #warunek zakonczenia dzialania algorytmu
			return tab
 
	for i in tab:  #dla wszystkich liczb w tablicy
#usun element jezeli jest podzielny przez obecna liczbe
		if (not(i%obecnie) and not(obecnie==i)) and obecnie!=1:
			tab.remove(i)
 
	i = tab.index(obecnie)+1
	obecnie = tab[i]
 
#pobierz od uzytkownika gorny zakres dzialania algorytmu i wypisz wyniki
n = int(raw_input("Podaj gorny zakres dzialania sita: "))
pierwsze = sito(n)
for pierwsza in pierwsze:
	print pierwsza