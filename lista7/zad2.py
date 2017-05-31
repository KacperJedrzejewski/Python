from itertools import permutations
def ile(slowo):
    tmp = {}
    for i in slowo:
        if i not in tmp:
            tmp[i] = 1 
        else:
            tmp[i] += 1
    return tmp

def czy_zawiera(slowo,slowo1)
    ile_slowo = {}
    ile_slowo = ile(slowo)
    ile_slowo1= {}
    ile_slowo1 = ile(j)
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
slownik1 = ['wsparł busole', 'połknij okrakiem','słał wieszczom','cenne wmieszał','ekspansja rzodkwi','obca makabra']
slownik_imion = ['bolesław prus','mikołaj kopernik','czesław miłosz']




for i in slownik_imion:
    znaki = ile(i)
    for j in slownik:
        znaki1 = ile(j)
        if czy_zawiera(i,j):
            if znaki.


odczolgac4grzezly1ubezdzwieczniwszy3zawlekajac