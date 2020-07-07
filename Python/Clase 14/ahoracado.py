#Ahorcado
import os
import random as r

print("Bienvenido al juego del Ahorcado!")

archivo = open("lemario-espanol.txt", "r")

palabras = []

for palabra in archivo:
    palabras.append(palabra)

posicion_aleatoria = r.randrange(0,len(palabras))
#print(">> " + palabras[posicion_aleatoria][:-1] + " >> " + str(posicion_aleatoria))

palabra_secreta = palabras[posicion_aleatoria][:-1]
letras_ingresadas = ""

vidas = 5
letras_ocultas = 0
letra = ""

while vidas > 0:
    letras_ocultas = 0

    # Mostrar palabra al usuario y contar letras ocultas
    for letra in palabra_secreta:
        if letra in letras_ingresadas:
            print(letra, end="")
        else:
            print("*", end="")
            letras_ocultas += 1
    
    # consultar si ganamos
    if letras_ocultas == 0:
        os.system("cls")
        print("\nEnbuenahora! Has Ganado Copito de nieve")
        break

    # INgresar letras
    tuletra = input("\nAdivine una letra: ")
    letras_ingresadas += tuletra

    # consultamos si existen en la palabra
    if tuletra not in palabra_secreta:
        vidas -= 1
        os.system("cls")
        print("\nOh No! te has equivocado, te quedan " + str(vidas) + " vidas")
    else:
        os.system("cls")
        print("\nCorrecto! sigue pequeño saltamotes")

    # en caso de terminar las vidas
    if vidas == 0:
        os.system("cls")
        print("\nHas fallado como ser Humano!!!, has perdido!")
        print("\nLa palabra secreta era: " + palabra_secreta)

print("\nNos vemos en otro juego")