import pygame
from colores import *
from constantes import *
from funciones import *


# Inicialización y ventana
pygame.init()
pantalla = pygame.display.set_mode(RESOLUCION_1)
COLOR_FONDO = GRIS  # Color de fondo general
pygame.display.set_caption("JuegoPY")


# Fuentes y textos de títulos
fuente = pygame.font.SysFont("arial", 100, True, True)
texto_pantalla = fuente.render("Pantalla Principal", True, COLOR_TEXTO_BOTON)
texto_pantalla_puntajes = fuente.render("Pantalla Puntajes", True, COLOR_TEXTO_BOTON)

# Posiciones centradas de títulos
ubicacion_texto_x = (pantalla.get_width() / 2) - (texto_pantalla.get_width() / 2)
ubicacion_texto_y = (pantalla.get_height() * 0.05)
ubicacion_texto_puntaje_x = (pantalla.get_width() / 2) - (texto_pantalla_puntajes.get_width() / 2)
ubicacion_texto_puntaje_y = (pantalla.get_height() * 0.05)


# Botones: medidas y posiciones (proporcionales)
# Ocupe 20% del ancho, 10% del alto y ubicado en el 2/3 del alto y centrado.
ancho_boton = pantalla.get_width() * 0.2
alto_boton = pantalla.get_height() * 0.1
x_boton = (pantalla.get_width() / 2) - (ancho_boton / 2)
y_boton = pantalla.get_height() * 0.50
y_boton_volver = pantalla.get_height() * 0.70
y_boton_jugar = pantalla.get_height() * 0.33
y_boton_salir = pantalla.get_height() * 0.66

# Rects de botones (x, y, ancho, alto)
rect_boton_puntaje = pygame.Rect(x_boton, y_boton, ancho_boton, alto_boton)
rect_boton_volver = pygame.Rect(x_boton, y_boton_salir, ancho_boton, alto_boton)
rect_boton_jugar = pygame.Rect(x_boton, y_boton_jugar, ancho_boton, alto_boton)
rect_boton_salir = pygame.Rect(x_boton, y_boton_salir, ancho_boton, alto_boton)


# Textos de botones (render + escala + rects)
texto_puntajes = fuente.render("Ver Puntajes", True, CELESTE)
texto_puntajes = pygame.transform.scale(texto_puntajes, (ancho_boton-5, alto_boton-5))
rect_texto_puntajes = texto_puntajes.get_rect()
rect_texto_puntajes.x = rect_boton_puntaje.x
rect_texto_puntajes.y = rect_boton_puntaje.y

texto_jugar = fuente.render("Jugar", True, VERDE)
texto_jugar = pygame.transform.scale(texto_jugar, (ancho_boton-5, alto_boton-5))
rect_texto_jugar = texto_jugar.get_rect()
rect_texto_jugar.x = rect_boton_jugar.x
rect_texto_jugar.y = rect_boton_jugar.y

texto_volver = fuente.render("Volver", True, ROJO)
texto_volver = pygame.transform.scale(texto_volver, (ancho_boton-5, alto_boton-5))
rect_texto_volver = texto_volver.get_rect()
rect_texto_volver.x = rect_boton_volver.x
rect_texto_volver.y = rect_boton_volver.y

texto_salir = fuente.render("Salir", True, AZUL)
texto_salir = pygame.transform.scale(texto_salir, (ancho_boton-5, alto_boton-5))
rect_texto_salir = texto_salir.get_rect()
rect_texto_salir.x = rect_boton_salir.x
rect_texto_salir.y = rect_boton_salir.y


# Rectángulo contenedor (pantalla juego)
rect_contenedor_y = int(pantalla.get_height() * 0.02)
rect_contenedor_ancho = int(pantalla.get_width() * 0.96 * 0.8)
rect_contenedor_alto = int(pantalla.get_height() * 0.96)
rect_contenedor_x = int(pantalla.get_width() - rect_contenedor_ancho - (pantalla.get_height() * 0.02))
rect_contenedor = pygame.Rect(rect_contenedor_x, rect_contenedor_y, rect_contenedor_ancho, rect_contenedor_alto)


# Construcción inicial del tablero

lista_color = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0), (150, 0, 120), (0, 200, 225)]

matriz = inicializar_matriz(CANTIDAD_FILAS, CANTIDAD_COLUMNAS) 
cargar_matriz_aleatoria(matriz, lista_color)  
crear_botones_matriz(matriz, rect_contenedor)  


# Banderas de estado
pantalla_actual = "principal"
corriendo = True


# Bucle principal
while corriendo:
    if pantalla_actual == "principal":
        # Eventos pantalla principal
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_boton_puntaje.collidepoint(evento.pos) == True:
                    pantalla_actual = "puntajes"  # cambia bandera de pantalla
                    print("Ingreso a puntajes")
                if rect_boton_jugar.collidepoint(evento.pos) == True:
                    pantalla_actual = "juego"     # cambia bandera de pantalla
                    print("Ingreso a juego")
                if rect_boton_salir.collidepoint(evento.pos) == True:
                    corriendo = False

        # Dibujo pantalla principal
        pantalla.fill(COLOR_FONDO)
        pantalla.blit(texto_pantalla, (ubicacion_texto_x, ubicacion_texto_y))
        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_puntaje, border_radius=15)  # Botón Puntajes
        pantalla.blit(texto_puntajes, rect_boton_puntaje)
        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_jugar, border_radius=15)    # Botón Jugar
        pantalla.blit(texto_jugar, rect_boton_jugar)
        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_salir, border_radius=15)    # Botón Salir
        pantalla.blit(texto_salir, rect_boton_salir)

    elif pantalla_actual == "puntajes":
        # Eventos pantalla puntajes
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_boton_volver.collidepoint(evento.pos) == True:
                    pantalla_actual = "principal"
                    print("Volvio a Principal")

        # Dibujo pantalla puntajes
        pantalla.fill(AMARILLO)
        pantalla.blit(texto_pantalla_puntajes, (ubicacion_texto_x, ubicacion_texto_y))
        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_volver, border_radius=15)
        pantalla.blit(texto_volver, rect_texto_volver)

    elif pantalla_actual == "juego":
        # Eventos pantalla juego
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Ejemplo: cambiar color de la celda clickeada
                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        if matriz[i][j]["rect"].collidepoint(evento.pos) == True:
                            from random import randint
                            matriz[i][j]["color"] = lista_color[randint(0, 5)]

        # Dibujo pantalla juego
        pantalla.fill((255, 255, 255))
        pygame.draw.rect(pantalla, (0, 0, 0), rect_contenedor, border_radius=15)
        dibujar_matriz(matriz, pantalla)

    # Refresco de pantalla
    pygame.display.flip()