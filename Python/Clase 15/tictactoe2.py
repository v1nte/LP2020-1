#tictactoe
import os
import random

"""
 X | O | O
 X | O | 
 X | X | O
"""

tablero = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]
]

def mostrar_tablero(t):
    print("Imprimir matriz con elementos iterables")
    for fila in t:
        for celda in fila:
            print(celda + "  ", end="")
        print("")
def espacio_disponible(p):
    if p<1 or p>9:
        return True
    if p==1:
        i=0
        j=0
    if p==2:
        i=0
        j=1
    if p==3:
        i=0
        j=2
    if p==4:
        i=1
        j=0
    if p==5:
        i=1
        j=1
    if p==6:
        i=1
        j=2
    if p==7:
        i=2
        j=0
    if p==8:
        i=2
        j=1
    if p==9:
        i=2
        j=2
    return tablero[i][j] in "XO"

def llenar_casilla(posicion, simbolo, t):
    if posicion==1: 
        t[0][0] = simbolo
        #print(">>[0][0]>> " + t[0][0])
    if posicion==2: 
        t[0][1] = simbolo
        #print(">>[0][1]>> " + t[0][1])
    if posicion==3: 
        t[0][2] = simbolo
        #print(">>[0][2]>> " + t[0][2])
    if posicion==4: 
        t[1][0] = simbolo
        ##print(">>[1][0]>> " + t[1][0])
    if posicion==5: 
        t[1][1] = simbolo
        #print(">>[1][1]>> " + t[1][1])
    if posicion==6: 
        t[1][2] = simbolo
        #print(">>[1][2]>> " + t[1][2])
    if posicion==7: 
        t[2][0] = simbolo
        #print(">>[2][0]>> " + t[2][0])
    if posicion==8: 
        t[2][1] = simbolo
        #print(">>[2][1]>> " + t[2][1])
    if posicion==9: 
        t[2][2] = simbolo
        #print(">>[2][2]>> " + t[2][2])
    return t

def verificar_empate(t):
    c = 0
    for i in range(len(t[0])):
        for j in range(len(t[0])):
            if tablero[i][j] not in "XO":
                c += 1
    return c==0

def verificar_ganador(s, t):
    g = False

    #Filas
    if t[0][0]==s and t[0][1]==s and t[0][2]==s:
        g = True
    if t[1][0]==s and t[1][1]==s and t[1][2]==s:
        g = True
    if t[2][0]==s and t[2][1]==s and t[2][2]==s:
        g = True
    
    #Columnas
    if t[0][0]==s and t[1][0]==s and t[2][0]==s:
        g = True
    if t[0][1]==s and t[1][1]==s and t[2][1]==s:
        g = True
    if t[0][2]==s and t[1][2]==s and t[2][2]==s:
        g = True
    
    #Diagonales
    if t[0][0]==s and t[1][1]==s and t[2][2]==s:
        g = True
    if t[0][2]==s and t[1][1]==s and t[2][0]==s:
        g = True

    return g
        
juego_en_ejecucion = True
alguien_gano = False
es_empate = False

while juego_en_ejecucion:
    os.system("cls")
    mostrar_tablero(tablero)
    movimiento_valido=True
    while(movimiento_valido):
        j1 = input("Jugador 1 (O) -> escoja una casilla: ")
        movimiento_valido = espacio_disponible(int(j1))
    tablero = llenar_casilla(int(j1),"O",tablero)

    alguien_gano = verificar_ganador("O",tablero)
    if alguien_gano:
        os.system("cls")
        mostrar_tablero(tablero)
        print("Felicidades! Jugador 1 (O) Has Ganado!!!")
        break
    es_empate = verificar_empate(tablero)

    os.system("cls")
    mostrar_tablero(tablero)
    movimiento_valido=True
    while(movimiento_valido):
        j2 = random.randrange(1,9)
        movimiento_valido = espacio_disponible(int(j2))
    tablero = llenar_casilla(int(j2),"X",tablero)
    
    alguien_gano = verificar_ganador("X", tablero)
    if alguien_gano:
        os.system("cls")
        mostrar_tablero(tablero)
        print("Felicidades! Jugador 2 (X) Has Ganado!!!")
        break
    es_empate = verificar_empate(tablero)

    if alguien_gano or es_empate:
        juego_en_ejecucion = False

print("Fin del juego")