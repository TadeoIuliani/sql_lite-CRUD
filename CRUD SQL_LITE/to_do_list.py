import sqlite3
from funciones_bd import *

prendido = True
while prendido:
    opcion = menu_principal()
    if opcion != 5:
        ejecutar_opcion(opcion)
    else:
        print("Gracias por jugar !!!")
        prendido = False
