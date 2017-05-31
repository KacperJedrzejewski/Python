
def ile(slowo):
    tmp = {}
    for i in slowo:
        if i not in tmp:
            tmp[i] = 1 
        else:
            tmp[i] += 1
    return tmp


def czy_zawiera(slowo,slowo1):
    ile_slowo = {}
    ile_slowo = ile(slowo)
    ile_slowo1= {}
    ile_slowo1 = ile(slowo1)
    control = 0
    for k in ile_slowo1 :
        if k not in ile_slowo:
            control = 1 
            break    
        elif ile_slowo1[k] > ile_slowo[k]:
            control = 1
            break
    if control == 1:
        return False
    return True    

slownik = open('slowa.txt').read().split('\n')

for i in slownik:
    for j in slownik:
                
        if czy_zawiera(i,j): 
            print(j,'sklada sie z ',i)

        
            