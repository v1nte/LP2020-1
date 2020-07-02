def doble(x):
    return x*2

#print("el doble de "+ str(3) + " es: "+str(doble(3)))

#expresion lambda
# lambda nombre_argumento : expresion

d = lambda x : x*2

#print("el doble de "+ str(3) + " es: "+str(d(3)))

pot = lambda b,e: b**e

#print(pot(3,2))

def potencia(e):
    return lambda n: n**e

cuadrado = potencia(2)
cubico = potencia(3)

print(cuadrado)
print(cubico(2))