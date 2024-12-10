from constantes import (TAMANO, RANKING_FILE)
from cuadricula import *
from rankings import *

# Funcion para jugar
def jugar():
    cuadricula = crear_cuadricula()

    for pais in paises:
        colocar_pais(cuadricula, pais)

    rellenar_con_letras(cuadricula)

    jugador = {
        "nombre": input("\nIngrese su nombre: "),
        "vidas": 3,
        "puntos": 0
    }

    print("")

    paises_encontrados = []

    while jugador["vidas"] > 0 and len(paises_encontrados) < len(paises):
        mostrar_cuadricula(cuadricula)

        if paises_encontrados:
            print("\nPaises encontrados:", ', '.join(paises_encontrados))
        else:
            print("\nNinguno")
        print(f"Vidas restantes: {jugador['vidas']}")
        
        pais = input("\nIngrese un pais: ").upper()

        if pais in paises_encontrados:
            print(f"¡Ya encontraste {pais}!")
            print("Intenta con otro.")
            continue

        if pais not in paises:
            jugador["vidas"] -= 1
            print(f"{pais} no está en la sopa de letras.")

        if verificar_pais(cuadricula, pais):
            paises_encontrados.append(pais)
            jugador["puntos"] += 1
            print(f"¡Correcto! Encontraste el pais: {pais}.")

    if jugador["vidas"] == 0:
        print("\n¡Te quedaste sin vidas!")
        print("Fin del juego.")
    elif len(paises_encontrados) == len(paises):
        print(f"\n¡Felicidades, {jugador['nombre']}! Encontraste todos los paises.")
        print(f"Tu puntuacion fue de: {jugador['puntos']}.")

    guardar_ranking(jugador["nombre"], jugador["puntos"])