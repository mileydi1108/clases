#primero tenemos que importar
#la funcion print (que viene del modulo)
#__future__ para poder utilizar a print
# como una funcion

from __future__ import print_function
def mi_funcion():
	print("hola mundo")


def nombres (nombre, apellido):
    nombre_completo= "mi nombre es %s %s y tengo %d" % (nombre, apellido, edad)
	print(nombre_completo)

nombres("Mileydi ", "Guerrero ", 24)