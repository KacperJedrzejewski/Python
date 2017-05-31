from math import fabs

def F(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3 * n + 1

def AnalizaCollatza(a,b):
	tmp1 = int ( fabs ( b - a ) )
	moc = [[] for x in range(tmp1) ]
	tmp = 0
	for i in range(tmp1):
		n = a + i
		moc[i] = 1
		while F(n) != 1 :
			n = F(n)
			moc[i] += 1
		tmp += moc[i]
	moc.sort()
	print (moc)
	if fabs( b - a ) % 2 == 0.0:
		return ( tmp / fabs ( b - a ), ( moc[ int( ( tmp1 - 1 ) / 2 ) ] + moc [ int ( tmp1 / 2 ) ] ) / 2 , moc[ int( tmp1 - 1 ) ] , moc[0] )
	else:
		return ( tmp / fabs ( b - a ), moc[ int(tmp1 / 2) ] , moc[int ( tmp1 - 1) ] , moc[0] )



wynik = [ [] for x in range(4) ]
wynik = AnalizaCollatza(10,20)
print('Srednia energii wynosi : ', wynik[0],'Mediana wynosi : ',wynik[1])
print('Max energi : ', wynik[2],'Min energi : ',wynik[3])oo