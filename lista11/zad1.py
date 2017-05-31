import locale
alfabet = {'a':0,'ą':1,'b':2,'c':3,'ć':4, 'd':5, 'e':6, 'ę':7, 'f':8, 'g':9, 'h':10, 'i':11, 'j':12, 'k':13, 'l':14, 'ł':15, 'm':16, 'n':17,'ń':18, 'o':19, 'ó':20, 'p':21, 'q':22, 'r':23, 's':24, 'ś':25, 't':26, 'u':27, 'v':28, 'w':29, 'x':30, 'y':31, 'z':32, 'ź':33, 'ż':34}

def cezar(napis, przesuniecie):
    zakodowany=""
    for i in napis:
    	zakodowany += str(lista [ ( alfabet[i] + przesuniecie ) % 35 ] )
    return zakodowany  


lista=list(alfabet.keys())
locale.setlocale(locale.LC_COLLATE, "pl_PL.UTF-8")
lista.sort(key=locale.strxfrm)

slowo = 'abcd'
print(slowo,cezar(slowo,1))