from itertools import permutations
def ile(slowo):
    tmp = {}
    for i in slowo:
        if i not in tmp:
            tmp[i] = 1 
        else:
            tmp[i] += 1
    return tmp

slownik = ['wsparł busole', 'połknij okrakiem','słał wieszczom','cenne wmieszał','ekspansja rzodkwi','obca makabra']
slownik_imion = ['bolesław prus','mikołaj kopernik','czesław miłosz']

for i in slownik:
    control = 0
    for j in slownik_imion:    
        if ile(i) == ile(j):
            print(i,'-',j)
            control = 1
            break
    if control == 0:
        print(i,'- ??') 



print(permutations('bolek'))


 