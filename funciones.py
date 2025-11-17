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