# Clase BASE 2
class obstaculo:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def herir(self, otro):
        print("He herido a "+otro.nombre)