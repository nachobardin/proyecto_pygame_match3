import pygame
from colores import * 
from constantes import * 
from funciones import * 

# Inicialización y ventana
pygame.init()
pantalla = pygame.display.set_mode(RESOLUCION_1)
COLOR_FONDO = GRIS
pygame.display.set_caption("JuegoPY")

# Fuentes
fuente = pygame.font.SysFont("arial", 100, True, True)
texto_pantalla = fuente.render("Pantalla Principal", True, COLOR_TEXTO_BOTON)
texto_pantalla_puntajes = fuente.render("Pantalla Puntajes", True, COLOR_TEXTO_BOTON)

# Posiciones de títulos
ubicacion_texto_x = (pantalla.get_width() / 2) - (texto_pantalla.get_width() / 2)
ubicacion_texto_y = pantalla.get_height() * 0.05
ubicacion_texto_puntaje_x = (pantalla.get_width() / 2) - (texto_pantalla_puntajes.get_width() / 2)
ubicacion_texto_puntaje_y = pantalla.get_height() * 0.05

# Botones
ancho_boton = pantalla.get_width() * 0.2
alto_boton = pantalla.get_height() * 0.1
x_boton = (pantalla.get_width() / 2) - (ancho_boton / 2)
y_boton_jugar = pantalla.get_height() * 0.33
y_boton_puntaje = pantalla.get_height() * 0.50
y_boton_salir = pantalla.get_height() * 0.70

# Rects botones
rect_boton_jugar = pygame.Rect(x_boton, y_boton_jugar, ancho_boton, alto_boton)
rect_boton_puntaje = pygame.Rect(x_boton, y_boton_puntaje, ancho_boton, alto_boton)
rect_boton_salir = pygame.Rect(x_boton, y_boton_salir, ancho_boton, alto_boton)
rect_boton_volver = pygame.Rect(x_boton, y_boton_salir, ancho_boton, alto_boton)

# Textos botones
def crear_texto_boton(texto, color):
    t = fuente.render(texto, True, color)
    t = pygame.transform.scale(t, (ancho_boton - 5, alto_boton - 5))
    return t

texto_jugar = crear_texto_boton("Jugar", VERDE)
texto_puntajes = crear_texto_boton("Puntajes", CELESTE)
texto_salir = crear_texto_boton("Salir", AZUL)
texto_volver = crear_texto_boton("Volver", ROJO)

rect_texto_jugar = texto_jugar.get_rect(center=rect_boton_jugar.center)
rect_texto_puntajes = texto_puntajes.get_rect(center=rect_boton_puntaje.center)
rect_texto_salir = texto_salir.get_rect(center=rect_boton_salir.center)
rect_texto_volver = texto_volver.get_rect(center=rect_boton_volver.center)

# Rect contenedor del tablero
rect_contenedor_y = int(pantalla.get_height() * 0.05)
rect_contenedor_ancho = int(pantalla.get_width() * 0.60)
rect_contenedor_alto = int(pantalla.get_height() * 0.90)
rect_contenedor_x = int(pantalla.get_width() * 0.35)
rect_contenedor = pygame.Rect(rect_contenedor_x, rect_contenedor_y, rect_contenedor_ancho, rect_contenedor_alto)

# Matriz (tablero)
lista_color = [ROJO, AZUL, VERDE, AMARILLO, CELESTE, GRIS]

matriz = inicializar_matriz(CANTIDAD_FILAS, CANTIDAD_COLUMNAS)
cargar_matriz_aleatoria(matriz, lista_color)
crear_botones_matriz(matriz, rect_contenedor)

# Estado
pantalla_actual = "principal"
primer_click = None
corriendo = True

# Bucle principal
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pantalla_actual == "principal": #Pantalla principal
                if rect_boton_jugar.collidepoint(evento.pos):
                    pantalla_actual = "juego"
                elif rect_boton_puntaje.collidepoint(evento.pos):
                    pantalla_actual = "puntajes"
                elif rect_boton_salir.collidepoint(evento.pos):
                    corriendo = False
            elif pantalla_actual == "puntajes": # Pantalla puntajes
                if rect_boton_volver.collidepoint(evento.pos):
                    pantalla_actual = "principal"
            elif pantalla_actual == "juego": # Pantalla juego
                for i in range(CANTIDAD_FILAS): # Busca que celda fue clickeada
                    for j in range(CANTIDAD_COLUMNAS):
                        if matriz[i][j]["rect"].collidepoint(evento.pos):
                            click_actual = (i, j)
                            if primer_click is None: # primer click
                                primer_click = click_actual
                            else:
                                segundo_click = click_actual
                                if primer_click == segundo_click: 
                                    primer_click = None
                                elif son_vecinos(primer_click, segundo_click):
                                    intercambiar(matriz, primer_click, segundo_click)
                                    if not hay_match(matriz):
                                        intercambiar(matriz, primer_click, segundo_click)
                                        print("Movimiento inválido, no hay match.")
                                    else:
                                        print("Match encontrado, movimiento válido.")
                                    primer_click = None
                                else:
                                    primer_click = segundo_click
                            break
                    else:
                          continue
                    break

    if pantalla_actual == "principal":
        pantalla.fill(COLOR_FONDO)
        pantalla.blit(texto_pantalla, (ubicacion_texto_x, ubicacion_texto_y))

        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_jugar, border_radius=15)
        pantalla.blit(texto_jugar, rect_texto_jugar)

        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_puntaje, border_radius=15)
        pantalla.blit(texto_puntajes, rect_texto_puntajes)

        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_salir, border_radius=15)
        pantalla.blit(texto_salir, rect_texto_salir)

    # PANTALLA PUNTAJES
    elif pantalla_actual == "puntajes":
        pantalla.fill(AMARILLO)
        pantalla.blit(texto_pantalla_puntajes, (ubicacion_texto_x, ubicacion_texto_y))

        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_volver, border_radius=15)
        pantalla.blit(texto_volver, rect_texto_volver)

    # PANTALLA JUEGO
    elif pantalla_actual == "juego":
        pantalla.fill(BLANCO)

        # Marco del tablero
        pygame.draw.rect(pantalla, GRIS, rect_contenedor, border_radius=15)

        # Dibujar caramelos
        dibujar_matriz(matriz, pantalla)

        # Resaltar celda seleccionada
        if primer_click is not None:
            r, c = primer_click
            pygame.draw.rect(pantalla, ROJO, matriz[r][c]["rect"], 8, border_radius=5)

    pygame.display.flip()

pygame.quit()
