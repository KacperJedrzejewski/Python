slowa = open('slowa.txt', 'r').read().split('\n')
tmp = {}

for slowo in slowa:
   tmp[slowo] = 0

for slowo in tmp:
    if slowo[::-1] in tmp:
        if tmp[slowo] == 0 and tmp[slowo[::-1]] == 0:
            print(slowo,slowo[::-1])
            tmp[slowo] = 1
            tmp[slowo[::-1]] = 1