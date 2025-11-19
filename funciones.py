import pygame
from random import *

def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial:any=None)->list[list]:
    matriz = []
    for _ in range(cant_filas):
        fila = []
        for _ in range(cant_columnas):
            fila.append(valor_inicial)
        matriz.append(fila)
    return matriz

def cargar_matriz_aleatoria(matriz: list[list], lista_color:list[tuple])->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = {"color":lista_color[randint(0, 5)]} # 0 - 5


def crear_botones_matriz(matriz:list[list], rect_cont:pygame.Rect)->None:
    ancho_celda_matriz = int(rect_cont.width * 0.96 / len(matriz[0])) # Ancho pantalla / cant_columnas
    alto_celda_matriz = int(rect_cont.height * 0.96 / len(matriz)) # Alto pantalla / cant_filas
    mitad_ancho_rect_cont = int(rect_cont.width * 0.02) + rect_cont.x
    mitad_alto_rect_cont = int(rect_cont.height * 0.02) + rect_cont.y
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            un_rectangulo = pygame.Rect((j * ancho_celda_matriz) + mitad_ancho_rect_cont, (i * alto_celda_matriz) + mitad_alto_rect_cont, ancho_celda_matriz, alto_celda_matriz)
            matriz[i][j].update({"rect": un_rectangulo})

def dibujar_matriz(matriz:list[list], pantalla:pygame.Surface)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            pygame.draw.rect(pantalla, matriz[i][j]["color"], matriz[i][j]["rect"])

def son_vecinos(a: tuple, b: tuple) -> bool:
#Devuelve True si las dos posiciones son adyacentes (arriba/abajo/izquierda/derecha)."""
    r1, c1 = a
    r2, c2 = b
    return (abs(r1 - r2) == 1 and c1 == c2) or (abs(c1 - c2) == 1 and r1 == r2)


def intercambiar(matriz: list[list], a: tuple, b: tuple) -> None:
    #Intercambia dos fichas de la matriz."""
    r1, c1 = a
    r2, c2 = b
    matriz[r1][c1]["color"], matriz[r2][c2]["color"] = matriz[r2][c2]["color"], matriz[r1][c1]["color"]


def buscar_matches(matriz: list[list]) -> set:
    """
    Busca coincidencias de 3 o más en filas y columnas.
    Devuelve un set con todas las posiciones que forman parte del match.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    celdas_en_match = set()

    # --- Buscar en filas ---
    for i in range(filas):
        contador = 1
        for j in range(1, columnas):
            if matriz[i][j]["color"] == matriz[i][j - 1]["color"]:
                contador += 1
            else:
                if contador >= 3:
                    for k in range(j - contador, j):
                        celdas_en_match.add((i, k))
                contador = 1

        if contador >= 3:
            for k in range(columnas - contador, columnas):
                celdas_en_match.add((i, k))

    # --- Buscar en columnas ---
    for j in range(columnas):
        contador = 1
        for i in range(1, filas):
            if matriz[i][j]["color"] == matriz[i - 1][j]["color"]:
                contador += 1
            else:
                if contador >= 3:
                    for k in range(i - contador, i):
                        celdas_en_match.add((k, j))
                contador = 1

        if contador >= 3:
            for k in range(filas - contador, filas):
                celdas_en_match.add((k, j))

    return celdas_en_match


def hay_match(matriz: list[list]) -> bool:
    """Devuelve True si existe un match de 3 o más en el tablero."""
    return len(buscar_matches(matriz)) > 0