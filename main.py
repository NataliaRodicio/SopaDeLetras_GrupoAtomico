import random
import string
import os
from constantes import (TAMANO, RANKING_FILE)
from rankings import *
from cuadricula import *
from jugabilidad import *

# Menu
def menu():
    while True:
        print('''
        Menu Principal

        1. Jugar
        2. Ver Ranking
        3. Salir''')

        print("")
        opcion = input("Selecciona una opcion (1/2/3): ")

        match opcion:
            case "1":
                jugar()
            case "2":
                ver_ranking()
            case "3":
                print("¡Nos vemos!")
                break
            case _:
                print("Opcion invalida.")
                print("Intenta de nuevo.")

menu()
