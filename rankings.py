import os
from constantes import *

# Guardar el puntaje en el archivo ranking
def guardar_ranking(nombre, puntaje):
    with open(RANKING_FILE, 'a') as f:
        f.write(f"{nombre} - {puntaje} puntos\n")

# Ver el ranking de jugadores
def ver_ranking():
    if os.path.exists(RANKING_FILE):
        with open(RANKING_FILE, 'r') as f:
            print(f.read())
    else:
        print("\nTodavia no hay ranking disponible.")