import locale
def cezar(napis, przesuniecie):
	zakodowany = ""
	for i in napis:
		zakodowany += str(lista [ ( alfabet[i] + przesuniecie ) % 35 ] )
	return zakodowany  

alfabet = {'a':0,'ą':1,'b':2,'c':3,'ć':4, 'd':5, 'e':6, 'ę':7, 'f':8, 'g':9, 'h':10, 'i':11, 'j':12, 'k':13, 'l':14, 'ł':15, 'm':16, 'n':17,'ń':18, 'o':19, 'ó':20, 'p':21, 'q':22, 'r':23, 's':24, 'ś':25, 't':26, 'u':27, 'v':28, 'w':29, 'x':30, 'y':31, 'z':32, 'ź':33, 'ż':34}
lista = alfabet.keys()
lista = list(lista)
locale.setlocale(locale.LC_COLLATE, "pl_PL.UTF-8")
lista.sort(key = locale.strxfrm)
slownik = open('slowa.txt').read().split('\n')
slownik.sort(key=len,reverse=True)

k,j = 0,1
sasiedzi = []

for i in slownik:
	i = i.lower()
	if '|'  in i or '-' in i or '#' in i or "'" in i or '_' in i:
		
		continue

	if sasiedzi != [] and len(sasiedzi[0]) != len(i) : 		
		while len(slownik[j]) == len(i) :
			j += 1 
		sasiedzi = slownik[k:j]
		k,j = j, j + 1
	elif sasiedzi == [] :
		sasiedzi = [i]
	


	for j in range(1,34):
		tmp = cezar(i,j)
		if tmp in sasiedzi:
			print(tmp)
			break


