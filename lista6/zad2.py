##############################################################
# Gra w życie (wersja 0.1)
##############################################################
from turtle import *

BOK = 15
tracer(0,1)
SX = 0
SY = 0

def kwadrat(x, y, kolor):
  fillcolor(kolor)
  pu()
  goto(SX + x * BOK, SY + y * BOK)
  pd()
  begin_fill()
  for i in range(4):
    fd(BOK)
    rt(90)
  end_fill() 

def rysuj(T):
  clear()
  for y in range(len(T)):
    for x in range(len(T[y])):
      if T[y][x] == '#':
        kolor = 'blue'
      elif T[y][x] == '*':
        kolor = 'red'
      elif T[y][x] == '!':
        kolor = 'green'
      elif T[y][x] == '@':  
        kolor = 'yellow'
      else:
        kolor = 'pink'
      kwadrat(x, y, kolor)
  update()    
      
def tablica(M, N):
  T = []
  for i in range(M):
    T.append( N * [0] )
  return T  
  
def sasiedzi(x,y, MX, MY,przenikanie):
  wynik = []
  if przenikanie == 0:

    if x == 0:
      L = [(-1,1), (1,1), (1,0), (0,1), (-1,0)]
    elif x == MX:
      L = [ (-1,-1), (1,-1), (1,0),(-1,0), (0,-1)]
    elif y == 0:
      L = [(1,1), (1,-1), (1,0), (0,1), (0,-1)]
    elif y == MY:
      L = [ (-1,-1), (-1,1), (0,1), (-1,0), (0,-1)]
    else: 
      L = [ (-1,-1), (-1,1), (1,1), (1,-1), (1,0), (0,1), (-1,0), (0,-1)] 
    
    for dx,dy in L:
      nx = (x+dx) % MX
      ny = (y+dy) % MY
      wynik.append( (nx,ny) )

  if przenikanie == 1:

    for dx,dy in [ (-1,-1), (-1,1), (1,1), (1,-1), (1,0), (0,1), (-1,0), (0,-1)]:
        nx = (x+dx) % MX
        ny = (y+dy) % MY
        wynik.append( (nx,ny) )
    
  return wynik

def nowe_pokolenieQuad(T,ileU,ileO):
  MY = len(T)
  MX = len(T[0])
  N = tablica(MY, MX)
  for y in range(MY):
    for x in range(MX):
      komorki = [0 for x in range(4)]
      komorkiZ = 0
      for nx,ny in sasiedzi(x,y, MX, MY,1):
        if T[ny][nx] == '#':
          komorki[0] += 1
        if T[ny][nx] == '*':
          komorki[1] += 1
        if T[ny][nx] == '!':
          komorki[2] += 1
        if T[ny][nx] == '@':
          komorki[3] += 1
        if T[ny][nx] in ['#','@','!','*']:
            komorkiZ += 1
      znaki=['#','*','!','@']  
      tmp = 0
      for i in range(4):
        if T[y][x] in znaki and komorkiZ in ileU:
            tmp = 1
            N[y][x] = T[y][x]
        elif T[y][x] in znaki:
            tmp = 1 
            N[y][x] = '.'
        elif T[y][x] == '.' and komorkiZ in ileO and (komorki[(i+1)%4] >= komorki[(i+2)%4] and komorki[(i+1)%4] >= komorki[(i+3)%4] and komorki[(i+1)%4] >= komorki[(i+4)%4]):
            N[y][x] = znaki[i]
            tmp = 1 
      if tmp != 1:
           N[y][x] = '.'
  return N

def nowe_pokolenie(T,ileU,ileO):
  MY = len(T)
  MX = len(T[0])
  N = tablica(MY, MX)
  for y in range(MY):
    for x in range(MX):
      komorki = [0 for i in range(2)]
      komorkiZ = 0
      tmp = 0
      znaki = ['#','*']
      for nx,ny in sasiedzi(x,y, MX, MY,1):
        if T[ny][nx] == '#':
          komorki[0] += 1
        if T[ny][nx] == '*':
          komorki[1] += 1    
        if T[ny][nx] in znaki:
          komorkiZ += 1
      for i in range(2):
        if T[y][x] in znaki and komorkiZ in ileU:
            tmp = 1
            N[y][x] = T[y][x]
        elif T[y][x] in znaki:
            tmp = 1 
            N[y][x] = '.'
        elif T[y][x] == '.' and komorkiZ in ileO and komorki[i] >= komorki[(i+1)%2]:
            N[y][x] = znaki[i]
            tmp = 1 
      if tmp != 1:
           N[y][x] = '.'
  return N


kolonia1 = """
..........................
..........................
..........................
........######............
..........................
..........................
.................***......
...................*......
..................*.......
....###...................
......#...................
.....#....................
..........................
..........................
.............###....***...
..............#.......*...
.##...........#......*....
..........................
..........................
""".split()[::-1]

kolonia = """
..........................
..........................
..........................
........######............
..........................
..........................
..........................
......!!!.................
........!.................
.......!.......@@@........
.................@........
................@.........
.....###..................
.......#..................
......#.............***...
...........###........*...
............#........*....
.##.........#.............
..........................
""".split()[::-1]
replikator = [[1,3,5,7],[1,3,5,7]]
labirynt = [[1,2,3,4,5],[3]]
miasta = [[2,3,4,5],[4,5,6,7,8]]
normal = [[2,3],[3]]
kolonia1 = list(map(list, kolonia1))

while True:
    
  rysuj(kolonia)
  kolonia = nowe_pokolenieQuad(kolonia,normal[0],normal[1])


input()