# POO

#class nombre:

class animal:
    """
    Que es esta clase
    """
    #atributos de la clase
    cabeza = True

    def __init__(self, especie, tipo, piel):
        # atributos del objeto/ instancia
        self.especie = especie
        self._tipo = tipo # privado
        self.__piel = piel # Privado
    
    # _ o __ privado
    # _ sigue siendo visible
    # __ no se registra como atributo

    def __str__(self):
        return "especie: "+self.especie+" tipo: "+self._tipo

    def getpiel(self):
        return self.__piel
    
simba = animal("Leon","felino","pelaje")

print(simba)

# Eliminacion de atributos u objetos
#del simba

print(simba)

#print(simba.getpiel())


