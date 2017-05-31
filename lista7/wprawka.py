
X = [14,43,12,763,324,50,42,11]
X1 = [1024,15,49,6,5]
def pierwsza(k):
    if k<2:
        return False
    i = 2
    for i in range(2, k):
        if k %  i == 0:
          return False
    return True

def najpopularniejsza(X):
    wynik = {}
    for i in X:
        if pierwsza(i):
            if i not in wynik:
                wynik[i] = 1 
            else:
                wynik[i] += 1
        else:
            for j in range(2,i):
                if pierwsza(j) and (i % j == 0):
                    k = 1 
                    while i % (j ** k) == 0 :
                        k += 1
                    if j not in wynik:
                        wynik[j] = k - 1
                    else:
                        wynik[j] += k - 1
    max = 0 
    for i in wynik:
        if wynik[i] > max:
            max = wynik[i]
            liczba = i 

    return liczba,max,wynik
print(najpopularniejsza(X1))
