# Importacion de Modulos
# from indica archivo
# as indica alias en e codigo local
from personaje import personaje as p
from obstaculo import obstaculo as o

# herencia : tomar elementos de una clase padre (madre o base) y entregarlas a clases hijos (o derivadas)

"""
class plomero:
    def __init__(self, nombre):
        self.nombre= nombre

    def saltar(self):
        print(self.nombre+" ha saltado!")

    def mover(self,direccion):
        print(self.nombre+" se mueve a la "+direccion)

class villano:
    def __init__(self, nombre):
        self.nombre= nombre

    def saltar(self):
        print(self.nombre+" ha saltado!")

    def mover(self,direccion):
        print(self.nombre+" se mueve a la "+direccion)

j1 = plomero("Mario")
j2 = plomero("Luigi")

j1.saltar()
j2.mover("derecha")

v1 = villano("Wario")
v1.saltar()
v1.mover("izquierda")

print(type(j1))
print(type(j2))
print(type(v1))
"""
"""
# Clase BASE
class personaje:
    def __init__(self, nombre):
        self.nombre= nombre

    def saltar(self):
        print(self.nombre+" ha saltado!")

    def mover(self,direccion):
        print(self.nombre+" se mueve a la "+direccion)

# Clase BASE 2
class obstaculo:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def herir(self, otro):
        print("He herido a "+otro.nombre)
"""
# Clases Derivadas
class plomero(p):
    pass

class villano(p):
    def __init__(self, nombre, nivel):
        #personaje.__init__(self,nombre) # redefinir
        super().__init__(nombre) # llamar elemento del Base
        self.nivel = nivel
    def __str__(self):
        return "nombre: "+self.nombre+" nivel: "+str(self.nivel)

class princesa(p):
    pass

class planta_carnivora(p,o):
    def saltar(self): # Override
        print("YO NO PUEDO SALTAR!")
    
    def mover(self, direccion): #Override
        print("Que yo no Me MUEVO!!!")

j1 = plomero("Mario")
j2 = plomero("Luigi")

v1 = villano("Wario",10)

p1 = princesa("Pitch")

pc1 = planta_carnivora("plantita")


j1 = plomero("Mario")
j2 = plomero("Luigi")

j1.saltar()
j2.mover("derecha")

v1.saltar()
v1.mover("izquierda")


p1.saltar()
p1.mover("izquierda")



pc1.saltar()
pc1.mover("izquierda")
pc1.herir(j1)

print(v1)
# definicion de atributos
#print(dir(pc1))

# obtener el tipo
#print(type(pc1))

# saber si es un tipo especifico
#print(isinstance(pc1,personaje))

# saber si una clase es subclase de otra
#print(issubclass(villano,personaje))