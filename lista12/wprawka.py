import locale

alfabet = {'a':0,'ą':1,'b':2,'c':3,'ć':4, 'd':5, 'e':6, 'ę':7, 'f':8, 'g':9, 'h':10, 'i':11, 'j':12, 'k':13, 'l':14, 'ł':15, 'm':16, 'n':17,'ń':18, 'o':19, 'ó':20, 'p':21, 'q':22, 'r':23, 's':24, 'ś':25, 't':26, 'u':27, 'v':28, 'w':29, 'x':30, 'y':31, 'z':32, 'ź':33, 'ż':34}
slownik = open('slowa.txt').read().split('\n')
slownik.sort(key = len,reverse = True)


def czy_rosnaca(slowo):
	licznik = 0 
	for i in slowo:
		tmp = i.lower()
		break
	for i in slowo:
		i = i.lower()
		licznik += 1 
		if licznik == 1:
			continue
		if '|'  in [i,tmp] or '-' in [i,tmp] or '#' in [i,tmp] or "'" in [i,tmp] or '_' in [i,tmp] or ':' in [i,tmp] or '+' in [i,tmp]:
			return False	
		if alfabet[i] < alfabet[tmp]  :
			return False
		tmp = i 
	return True 


licznik = 0 
for i in slownik:

	if(czy_rosnaca(i)):
		print(i)
		licznik += 1 
	if licznik >= 10 :
		break