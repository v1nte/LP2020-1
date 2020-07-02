import os

#manejo de archivo

#Lectura
#open(<ruta/archivo>,<tipo>)
""" Opciones de apertura
r - leer, es por defecto y no crea nuevos archivos si no existe el indicado (error)
a - agrega al final texto, crea archivo
w - sobreescribe un archivo, crea un archivo
x - crear un archivo, retorna un error si el archivo indicado existe

opciones de tipo de texto
t - texto, viene por defecto
b - Binario (ej: imagen)
"""

#Excepciones
try:
    archivo = open("in.txt", "r")
    #print(w)
except NameError:
    print("La variable no estaba inciada")
except:
    print("no es posible abrir el archivo")
finally:
    archivo.close()
    print("Sin problemas")
#else:
#    print("Sin Problemas")

#print(archivo.read())
# read(limitador)
#print(archivo.read(10))
#lineas de texto
#print(archivo.readline())
#print(archivo.readline())

#for x in archivo.readlines():
#    print(x)

#Escritura / Creacion
#archivo2 = open("in2.txt","x")
#archivo2 = open("in2.txt","w")
#archivo2 = open("in2.txt","a")
#archivo2.write("Quedan pocos minutos para terminar la clase")
#archivo2.write("Y aun necesito mas tiempo")

#Eliminacion
#os.remove("in2.txt")
