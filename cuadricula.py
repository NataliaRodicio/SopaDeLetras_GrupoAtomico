import random
import string
from constantes import (TAMANO, RANKING_FILE)

# Crear cuadricula
def crear_cuadricula():
    fila = [' ' for i in range(TAMANO)]

    sopa = []
    for i in range(TAMANO):
        sopa.append(fila.copy())

    return sopa

# Colocar pais en la cuadricula
def colocar_pais(cuadricula, pais):
    direccion = random.choice(['horizontal', 'vertical', 'diagonal'])
    pais = pais.upper()
    
    for _ in range(100):
        fila = random.randint(0, TAMANO - 1)
        columna = random.randint(0, TAMANO - 1)

        if direccion == 'horizontal' and columna + len(pais) <= TAMANO:
            
            espacio_libre = True
            for i in range(len(pais)):
                if cuadricula[fila][columna + i] != ' ':
                    espacio_libre = False
                    break
            if espacio_libre:
                for i in range(len(pais)):
                    cuadricula[fila][columna + i] = pais[i]
                return

        elif direccion == 'vertical' and fila + len(pais) <= TAMANO:
            
            espacio_libre = True
            for i in range(len(pais)):
                if cuadricula[fila + i][columna] != ' ':
                    espacio_libre = False
                    break
            if espacio_libre:
                for i in range(len(pais)):
                    cuadricula[fila + i][columna] = pais[i]
                return

        elif direccion == 'diagonal' and fila + len(pais) <= TAMANO and columna + len(pais) <= TAMANO:
            
            espacio_libre = True
            for i in range(len(pais)):
                if cuadricula[fila + i][columna + i] != ' ':
                    espacio_libre = False
                    break
            if espacio_libre:
                for i in range(len(pais)):
                    cuadricula[fila + i][columna + i] = pais[i]
                return

# Rellenar la cuadricula con letras aleatorias
def rellenar_con_letras(cuadricula):
    for i in range(TAMANO):
        for j in range(TAMANO):
            if cuadricula[i][j] == ' ':
                cuadricula[i][j] = random.choice(string.ascii_uppercase)

# Mostrar la cuadricula en la terminal
def mostrar_cuadricula(cuadricula):
    for letra in cuadricula:
        print(' '.join(letra))

# Verificar si un pais esta en la cuadricula
def verificar_pais(cuadricula, pais):
    pais = pais.upper()
    for i in range(TAMANO):
        for j in range(TAMANO):
            # Horizontal
            if j + len(pais) <= TAMANO:
                encontrado = True
                for letra in range(len(pais)):
                    if cuadricula[i][j + letra] != pais[letra]:
                        encontrado = False
                        break
                if encontrado:
                    return True

            # Vertical
            if i + len(pais) <= TAMANO:
                encontrado = True
                for letra in range(len(pais)):
                    if cuadricula[i + letra][j] != pais[letra]:
                        encontrado = False
                        break
                if encontrado:
                    return True

            # Diagonal
            if i + len(pais) <= TAMANO and j + len(pais) <= TAMANO:
                encontrado = True
                for letra in range(len(pais)):
                    if cuadricula[i + letra][j + letra] != pais[letra]:
                        encontrado = False
                        break
                if encontrado:
                    return True
    return False

