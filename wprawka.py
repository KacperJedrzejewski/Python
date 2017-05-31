def Rysuj_kwadraty(n,duzy,maly):
    for i in range(1,duzy):
        if i == 1:
            for j in range(n):
                print(duzy * '#',maly * ' ',sep='',end='')
            print()    
        elif (duzy - maly) - i > 0:
                       for j in range(n):
                           print('#',(duzy-2) *' ','#',maly *' ',sep='',end='')
                       print()    
        elif (duzy-maly) - i == 0:
            for j in range(n):
                print('#',(duzy-2)*' ','#',maly*'#',sep='',end='')
            print()    
        else:
            for j in range(n):
                print('#',(duzy-2)*' ','##',(maly-2)*' ','#',sep='',end='')
            print()   
                
    for j in range(n):
      print(duzy * '#',maly * '#',sep='',end='')
    print()                
     
        
                 
        
Rysuj_kwadraty(4,8,4)        
