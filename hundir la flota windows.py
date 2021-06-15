from os import system

def numerar(let):
  if let=="A":
    return 0
  elif let=="B":
    return 1
  elif let=="C":
    return 2
  elif let=="D":
    return 3
  elif let=="E":
    return 4
  elif let=="F":
    return 5
  elif let=="G":
    return 6
  elif let=="H":
    return 7

def mapeado(mapa,elegir):
  
  print(elegir.center(57,"="))
  print("\n\n")
  print(s+"0"+s+"1"+s+"2"+s+"3"+s+"4"+s+"5"+s+"6"+s+"7")
  print("\n")
  print("A"+sl+str(mapa[0][0])+s+str(mapa[0][1])+s+str(mapa[0][2])+s+str(mapa[0][3])+s+str(mapa[0][4])+s+str(mapa[0][5])+s+str(mapa[0][6])+s+str(mapa[0][7]))
  print("\n")
  print("B"+sl+str(mapa[1][0])+s+str(mapa[1][1])+s+str(mapa[1][2])+s+str(mapa[1][3])+s+str(mapa[1][4])+s+str(mapa[1][5])+s+str(mapa[1][6])+s+str(mapa[1][7]))
  print("\n")
  print("C"+sl+str(mapa[2][0])+s+str(mapa[2][1])+s+str(mapa[2][2])+s+str(mapa[2][3])+s+str(mapa[2][4])+s+str(mapa[2][5])+s+str(mapa[2][6])+s+str(mapa[2][7]))
  print("\n")
  print("D"+sl+str(mapa[3][0])+s+str(mapa[3][1])+s+str(mapa[3][2])+s+str(mapa[3][3])+s+str(mapa[3][4])+s+str(mapa[3][5])+s+str(mapa[3][6])+s+str(mapa[3][7]))
  print("\n")
  print("E"+sl+str(mapa[4][0])+s+str(mapa[4][1])+s+str(mapa[4][2])+s+str(mapa[4][3])+s+str(mapa[4][4])+s+str(mapa[4][5])+s+str(mapa[4][6])+s+str(mapa[4][7]))
  print("\n")
  print("F"+sl+str(mapa[5][0])+s+str(mapa[5][1])+s+str(mapa[5][2])+s+str(mapa[5][3])+s+str(mapa[5][4])+s+str(mapa[5][5])+s+str(mapa[5][6])+s+str(mapa[5][7]))
  print("\n")
  print("G"+sl+str(mapa[6][0])+s+str(mapa[6][1])+s+str(mapa[6][2])+s+str(mapa[6][3])+s+str(mapa[6][4])+s+str(mapa[6][5])+s+str(mapa[6][6])+s+str(mapa[6][7]))
  print("\n")
  print("H"+sl+str(mapa[7][0])+s+str(mapa[7][1])+s+str(mapa[7][2])+s+str(mapa[7][3])+s+str(mapa[7][4])+s+str(mapa[7][5])+s+str(mapa[7][6])+s+str(mapa[7][7]))
  print("\n\n\n"+error)

def mapeado_marcado(mapa,turno):
  
  print(turno.center(57,"="))
  print("\n\n")
  print(s+"0"+s+"1"+s+"2"+s+"3"+s+"4"+s+"5"+s+"6"+s+"7")
  print("\n")
  print("A"+sl+str(mapa[0][0])+s+str(mapa[0][1])+s+str(mapa[0][2])+s+str(mapa[0][3])+s+str(mapa[0][4])+s+str(mapa[0][5])+s+str(mapa[0][6])+s+str(mapa[0][7]))
  print("\n")
  print("B"+sl+str(mapa[1][0])+s+str(mapa[1][1])+s+str(mapa[1][2])+s+str(mapa[1][3])+s+str(mapa[1][4])+s+str(mapa[1][5])+s+str(mapa[1][6])+s+str(mapa[1][7]))
  print("\n")
  print("C"+sl+str(mapa[2][0])+s+str(mapa[2][1])+s+str(mapa[2][2])+s+str(mapa[2][3])+s+str(mapa[2][4])+s+str(mapa[2][5])+s+str(mapa[2][6])+s+str(mapa[2][7]))
  print("\n")
  print("D"+sl+str(mapa[3][0])+s+str(mapa[3][1])+s+str(mapa[3][2])+s+str(mapa[3][3])+s+str(mapa[3][4])+s+str(mapa[3][5])+s+str(mapa[3][6])+s+str(mapa[3][7]))
  print("\n")
  print("E"+sl+str(mapa[4][0])+s+str(mapa[4][1])+s+str(mapa[4][2])+s+str(mapa[4][3])+s+str(mapa[4][4])+s+str(mapa[4][5])+s+str(mapa[4][6])+s+str(mapa[4][7]))
  print("\n")
  print("F"+sl+str(mapa[5][0])+s+str(mapa[5][1])+s+str(mapa[5][2])+s+str(mapa[5][3])+s+str(mapa[5][4])+s+str(mapa[5][5])+s+str(mapa[5][6])+s+str(mapa[5][7]))
  print("\n")
  print("G"+sl+str(mapa[6][0])+s+str(mapa[6][1])+s+str(mapa[6][2])+s+str(mapa[6][3])+s+str(mapa[6][4])+s+str(mapa[6][5])+s+str(mapa[6][6])+s+str(mapa[6][7]))
  print("\n")
  print("H"+sl+str(mapa[7][0])+s+str(mapa[7][1])+s+str(mapa[7][2])+s+str(mapa[7][3])+s+str(mapa[7][4])+s+str(mapa[7][5])+s+str(mapa[7][6])+s+str(mapa[7][7]))
  print("\n\n\n"+error)

def explosion(mapa_m,mapa,vida_barco):
  for x in range(mx):
    for y in range(my):
      if mapa_m[x][y] == "X" and vida_barco[int(mapa[x][y])-1]==0:
        mapa_m[x][y]=str(mapa[x][y])

s="      "
sl="     "
elegir_1="JUGADOR 1 COLOCA TUS BARCOS"
elegir_2="JUGADOR 2 COLOCA TUS BARCOS"
turn1="TU TURNO JUGADOR 1"
turn2="TU TURNO JUGADOR 2"

mapa1=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]
mx=8
my=8

l_barcos=[2,2]
ultimo=False
pos=0
error=""
while True:

  for x in range(mx):
    for y in range(my):
      if mapa1[x][y] == 0:
        mapa1[x][y]="■"

  while True:
    mapeado(mapa1,elegir_1)
    error=""
    p=input("PON LAS CASILLAS PARA TU BARCO: LONGITUD ("+str(l_barcos[pos])+")\n\n").split()
    x1=""
    x2=""
    lon=0
    libre=True
    posicion=True
    for x in p:
      posx=numerar(str(x[0]).upper())
      posy=int(x[1])
      x1+=str(posx)
      x2+=str(posy)
      if mapa1[posx][posy]!="■":
        libre=False
      lon+=len(x)
    if x1.count(x1[0])<len(x1) and x2.count(x2[0])<len(x2):
      posicion=False
    if x1.count(x1[0])<len(x1):
      l=[int(x) for x in x1]
      for x in l:
        if x+1 not in l and x-1 not in l:
          posicion=False
    if x2.count(x2[0])<len(x2):
      l=[int(x) for x in x2]
      for x in l:
        if x+1 not in l and x-1 not in l:
          posicion=False

    if len(p)==l_barcos[pos] and lon==2*l_barcos[pos] and libre and posicion:
      for x in p:
        posx=numerar(str(x[0]).upper())
        posy=int(x[1])
        mapa1[posx][posy]=pos+1
        
      system("cls")
      break
    else:
      error="ERROR: BARCO DE " +str(l_barcos[pos])+" CASILLAS"
      if posicion==False:
        error="ERROR: EL BARCO NO ESTA RECTO"
      if libre==False:
        error="ERROR: ESTAS CASILLAS ESTAN OCUPADAS"
      if lon!=2*l_barcos[pos]:
        error="ERROR: CASILLAS NO ENCONTRADAS"
      system("cls")
  pos+=1
  if ultimo:
    pos=len(l_barcos)
  system("cls")
  if pos==len(l_barcos):
    mapeado(mapa1,elegir_1)
    error=""
    e=str(input("JUGADOR 1 ESTAS LISTO PARA EMPEZAR? (s/n)\n"))
    system("cls")
    if e=="n":
      mapeado(mapa1,elegir_1)
      error=""
      while True:
        try:
          quit_barcos=int(input("Que barco quieres quitar? "))
          break
        except:
          system("cls")
          mapeado(mapa1,elegir_1)
          error=""
      system("cls")
      pos=quit_barcos-1
      for x in range(mx):
        for y in range(my):
          if mapa1[x][y] == quit_barcos:
            mapa1[x][y]="■"
      ultimo=True
    else:
      break



mapa2=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]

pos=0
error=""
ultimo=False

while True:

  for x in range(mx):
    for y in range(my):
      if mapa2[x][y] == 0:
        mapa2[x][y]="■"

  while True:
    mapeado(mapa2,elegir_2)
    error=""
    p=input("PON LAS CASILLAS PARA TU BARCO: LONGITUD ("+str(l_barcos[pos])+")\n\n").split()
    x1=""
    x2=""
    lon=0
    libre=True
    posicion=True
    for x in p:
      posx=numerar(str(x[0]).upper())
      posy=int(x[1])
      x1+=str(posx)
      x2+=str(posy)
      if mapa2[posx][posy]!="■":
        libre=False
      lon+=len(x)
    if x1.count(x1[0])<len(x1) and x2.count(x2[0])<len(x2):
      posicion=False
    if x1.count(x1[0])<len(x1):
      l=[int(x) for x in x1]
      for x in l:
        if x+1 not in l and x-1 not in l:
          posicion=False
    if x2.count(x2[0])<len(x2):
      l=[int(x) for x in x2]
      for x in l:
        if x+1 not in l and x-1 not in l:
          posicion=False

    if len(p)==l_barcos[pos] and lon==2*l_barcos[pos] and libre and posicion:
      for x in p:
        posx=numerar(str(x[0]).upper())
        posy=int(x[1])
        mapa2[posx][posy]=pos+1

      system("cls")
      break
    else:
      error="ERROR: BARCO DE " +str(l_barcos[pos])+" CASILLAS"
      if posicion==False:
        error="ERROR: EL BARCO NO ESTA RECTO"
      if libre==False:
        error="ERROR: ESTAS CASILLAS ESTAN OCUPADAS"
      if lon!=2*l_barcos[pos]:
        error="ERROR: CASILLAS NO ENCONTRADAS"
      system("cls")
  pos+=1
  if ultimo:
    pos=len(l_barcos)
  system("cls")
  if pos==len(l_barcos):
    mapeado(mapa2,elegir_2)
    error=""
    e=str(input("JUGADOR 2 ESTAS LISTO PARA EMPEZAR? (s/n)\n"))
    system("cls")
    if e=="n":
      mapeado(mapa2,elegir_2)
      error=""
      while True:
        try:
          quit_barcos=int(input("Que barco quieres quitar? "))
          break
        except:
          system("cls")
          mapeado(mapa2,elegir_2)
          error=""
      system("cls")
      pos=quit_barcos-1
      for x in range(mx):
        for y in range(my):
          if mapa2[x][y] == quit_barcos:
            mapa2[x][y]="■"
      ultimo=True
    else:
      break


mapa1_marcados=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]

mapa2_marcados=[
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]

vida_barcos1=l_barcos
vida_barcos2=l_barcos

turno=True

for x in range(mx):
  for y in range(my):
    if mapa1_marcados[x][y] == 0:
      mapa1_marcados[x][y]="■"

for x in range(mx):
  for y in range(my):
    if mapa2_marcados[x][y] == 0:
      mapa2_marcados[x][y]="■"

while True:
  if turno:
    explosion(mapa2_marcados,mapa2,vida_barcos2)
    system("cls")
    mapeado_marcado(mapa2_marcados,turn1)
    error=""
    
    while True:
      a=str(input())
      try:
        if len(a)<3 and int(numerar(a[0].upper()))<=7 and int(a[1])<=7:
          posx=int(numerar(a[0].upper()))
          posy=int(a[1])
          break
        else:
          system("cls")
          error="CASILLA NO ENCONTRADA"
          mapeado_marcado(mapa2_marcados,turn1)
          error=""
      except:
        system("cls")
        error="CASILLA NO ENCONTRADA"
        mapeado_marcado(mapa2_marcados,turn1)
        error=""

    if mapa2_marcados[posx][posy]=="■":
      if mapa2[posx][posy]!="■":
        mapa2_marcados[posx][posy]="X"
        vida_barcos2[int(mapa2[posx][posy])-1]-=1
      else:
        mapa2_marcados[posx][posy]="-"
        error="FALLO"
        turno=False
    else:
      error="YA HAS PUESTO ESA CASILLA"
    if sum(vida_barcos2)==0:
      explosion(mapa2_marcados,mapa2,vida_barcos2)
      system("cls")
      error="FELICIDADES JUGADOR 1"
      mapeado_marcado(mapa2_marcados,"HA GANADO EL JUGADOR 1")
      break


  else:
    explosion(mapa1_marcados,mapa1,vida_barcos1)
    system("cls")
    mapeado_marcado(mapa1_marcados,turn2)
    error=""

    while True:
      a=str(input())
      try:
        if len(a)<3 and int(numerar(a[0].upper()))<=7 and int(a[1])<=7:
          posx=int(numerar(a[0].upper()))
          posy=int(a[1])
          break
        else:
          system("cls")
          error="CASILLA NO ENCONTRADA"
          mapeado_marcado(mapa1_marcados,turn2)
          error=""          
      except:
        system("cls")
        error="CASILLA NO ENCONTRADA"
        mapeado_marcado(mapa1_marcados,turn2)
        error=""

    if mapa1_marcados[posx][posy]=="■":
      if mapa1[posx][posy]!="■":
        mapa1_marcados[posx][posy]="X"
        vida_barcos1[int(mapa1[posx][posy])-1]-=1
      else:
        mapa1_marcados[posx][posy]="-"
        error="FALLO"
        turno=True

    else:
      error="YA HAS PUESTO ESA CASILLA"
    if sum(vida_barcos1)==0:
      explosion(mapa1_marcados,mapa1,vida_barcos1)
      system("cls")
      error="FELICIDADES JUGADOR 2"
      mapeado_marcado(mapa1_marcados,"HA GANADO EL JUGADOR 2")
      break