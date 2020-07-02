# Clase BASE
class personaje:
    def __init__(self, nombre):
        self.nombre= nombre

    def saltar(self):
        print(self.nombre+" ha saltado!")

    def mover(self,direccion):
        print(self.nombre+" se mueve a la "+direccion)