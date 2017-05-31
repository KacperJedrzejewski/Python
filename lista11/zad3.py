def permutacje_liczbowe(slowo):
	i,i1 = 1,1
	tmp = "" 
	for j in slowo:
		if j not in tmp and tmp == "":
			tmp += j
			wynik = str(i) 
			i += 1
		elif j not in tmp :
			tmp += j
			wynik +=  '-' + str(i) 
			i += 1
		else :
			i1 = 1
			for k in tmp: 
				if k != j :
					i1 += 1 
				else:
					break
			wynik +=  '-' + str(i1)
	return wynik

slowo = 'indianin'
print(slowo, permutacje_liczbowe(slowo))
