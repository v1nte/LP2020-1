texto = "este es un texto"
print(len(texto))
"""
t_array= texto.split(" ")

print(t_array)

x = "cadena" in texto
print(x)

"""

texto_largo = """
este es un texto largo
de varias lineas
que se pueden almacenar
en una variable
"""
print(texto_largo)

t1 = ">> siguiente texto: " + texto
print(t1)

edad = 30
t2 = "felicidades por tus {} {} {} {}años"
print(t2.format(edad,edad+1,edad+2,edad+3))

nuevo_texto = texto.replace("un","el")

print(nuevo_texto)