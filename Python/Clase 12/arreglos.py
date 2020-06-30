# Arrays
# List -> es una coleccion ordenada y podemos reordenar (cambiar de posicion)

#lista = ["Vicente", "Lorenzo", "Manuel", "Fran", "Victor", "Diego", "Lucas", "Pedrito"]
#lista = list(("Vicente", "Lorenzo", "Manuel", "Fran", "Victor", "Diego", "Lucas", "Pedrito"))

#lista.append("Joel")
#lista.insert(0,"Joel")

#lista.remove("Vicente")
#del lista[0]

#lista.clear()

#PILA
#print(lista.pop())

# sort(reverse = bool, key= Funcion)
# False -> Ascendente
# True -> Descendente
#lista.sort(reverse=True) # ordena
#lista.reverse()
#print(lista)


# TUPLAS -> tiene un orden inmutable
"""
t1 = ("Lucas", 20)
t2 = ("Vicente", 20)
t3 = ("Joel", 29)
t4 = ("Fran", 22)

tuplas = [t1,t2,t3,t4]
print(tuplas)

print(tuplas[0].index("Lucas"))
"""

# Sets -> no tienen un orden y no tienen indices

conjunto = {"lapiz", "goma","cuaderno"}
"""
print(conjunto)

for x in conjunto:
    print(x)
"""
#adicionar
#conjunto.add("taladro")
#conjunto.update(["taladro","broca","cepillo"])

#eliminar
"""
conjunto.discard("cuaderno")

conjunto2 = {1,2,3,4,5}

conjunto_grande = conjunto.union(conjunto2)

print(conjunto_grande)
"""

# Diccionarios -> no tienen orden, pero tienen idexación y son intercambiables

diccionario = {
    "rut" : 17641354,
    "nombre" : "Joel",
    "edad" : 29
}
"""
#print(diccionario["nombre"])

x = diccionario.get("nombre")
#print(x)

#for i in diccionario.values():
#    print(i)

    
for i,j in diccionario.items():
    print(i, j)

"""
super_diccionario = {
    "persona1":{
        "nombre": "Joel",
        "edad": 29
    },
    "persona2":{
        "nombre": "Vicente",
        "edad": 20
    },
    "persona3":{
        "nombre": "Fran",
        "edad": 22
    },
    "persona4":{
        "nombre": "Lorenzo",
        "edad": 22
    }
}

#print(super_diccionario["persona1"].values())

print(diccionario.keys())