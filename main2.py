import pygame
from modulos.constantes import *
from modulos.funciones import *

# Inicialización de la ventana principal
pygame.init()
pygame.display.set_icon(LOGO)  # Carga el icono de la ventana 
pygame.display.set_caption(TITULO_JUEGO) # Titulo de la ventana principal

# Pantalla y resolucion
RESOLUCIONES = [(800, 600), (1024, 768), (1280, 720)]
indice_resolucion = 0  
pantalla = pygame.display.set_mode(RESOLUCIONES[indice_resolucion])  # Se crea la pantalla con la resolucion inicial

# Musica del juego
pygame.mixer.music.load(SONIDO_MENU)
pygame.mixer.music.set_volume(VOL_MUSICA)  # Se define el volumen de la musica
pygame.mixer.music.play(-1)    # Se reproduce la música en loop infinito.

# Fuentes
fuente_timer = pygame.font.SysFont("arial", 30)                # Fuente para timer.
fuente_titulo = pygame.font.SysFont("arial", 100, True, True)  # Fuente grande para títulos.
fuente_puntaje = pygame.font.SysFont("arial", 40)              # Fuente mediana para puntajes.
fuente_input = pygame.font.SysFont("arial", 40)                # Fuente para input de nombre de usuario.

# Carga y escalado de fondos para que se ajusten a la pantalla actual
tam_actual_pantalla = pantalla.get_size()  # Tupla (ancho, alto)
FONDO_PANTALLA_PRINCIPAL = escalar_fondo(RUTA_FONDO_PRINCIPAL, tam_actual_pantalla)
FONDO_PUNTAJES = escalar_fondo(RUTA_FONDO_PUNTAJES, tam_actual_pantalla)
FONDO_JUEGO = escalar_fondo(RUTA_FONDO_JUEGO, tam_actual_pantalla)
FONDO_REGISTRO = escalar_fondo(RUTA_FONDO_REGISTRO, tam_actual_pantalla)

# Tamanios y posiciones de botones
ancho_boton = pantalla.get_width() * 0.20  # Los botones ocupan el 20% del ancho de pantalla
alto_boton = pantalla.get_height() * 0.08  # Los botones ocupan el 8% del alto de pantalla
x_boton = (pantalla.get_width() / 2) - (ancho_boton / 2)  # Centrado horizontal

# Posiciones verticales de botones
y_boton_jugar      = pantalla.get_height() * 0.45  # 45% desde arriba para el botón "Jugar"
y_boton_puntaje    = pantalla.get_height() * 0.60  # 60% desde arriba para "Puntajes"
y_boton_resolucion = pantalla.get_height() * 0.75  # 75% para "Resolución"
y_boton_salir      = pantalla.get_height() * 0.90  # 90% para "Salir"

# Creacion de los rectángulos para cada botón
rect_boton_jugar      = pygame.Rect(x_boton, y_boton_jugar, ancho_boton, alto_boton)
rect_boton_puntaje    = pygame.Rect(x_boton, y_boton_puntaje, ancho_boton, alto_boton)
rect_boton_resolucion = pygame.Rect(x_boton, y_boton_resolucion, ancho_boton, alto_boton)
rect_boton_salir      = pygame.Rect(x_boton, y_boton_salir, ancho_boton, alto_boton)
rect_boton_volver     = pygame.Rect(x_boton, y_boton_salir, ancho_boton, alto_boton) 
rect_boton_reiniciar  = pygame.Rect(x_boton, y_boton_salir, ancho_boton, alto_boton)

# Carga de las imágenes de los botones, escalándolas al tamanio de los botones
img_btn_jugar      = colocar_img_boton(RUTA_JUGAR_BTN, ancho_boton, alto_boton)
img_btn_puntajes   = colocar_img_boton(RUTA_PUNTAJES_BTN, ancho_boton, alto_boton)
img_btn_resolucion = colocar_img_boton(RUTA_RESOLUCION_BTN, ancho_boton, alto_boton)
img_btn_salir      = colocar_img_boton(RUTA_SALIR_BTN, ancho_boton, alto_boton)
img_btn_volver     = colocar_img_boton(RUTA_VOLVER_BTN, ancho_boton, alto_boton)
img_btn_reiniciar  = colocar_img_boton(RUTA_REINICIAR_BTN, ancho_boton, alto_boton)

# Centra las imágenes dentro de sus respectivos botones
rect_img_jugar      = img_btn_jugar.get_rect(center=rect_boton_jugar.center)
rect_img_puntajes   = img_btn_puntajes.get_rect(center=rect_boton_puntaje.center)
rect_img_resolucion = img_btn_resolucion.get_rect(center=rect_boton_resolucion.center)
rect_img_salir      = img_btn_salir.get_rect(center=rect_boton_salir.center)
rect_img_volver     = img_btn_volver.get_rect(center=rect_boton_volver.center)
rect_img_reiniciar    = img_btn_reiniciar.get_rect(center=rect_boton_reiniciar.center)

# Timer escalado
ancho_timer = pantalla.get_width() * 0.18
alto_timer = pantalla.get_height() * 0.12
img_timer = colocar_img_boton(RUTA_TIMER_BTN, ancho_timer, alto_timer)

# Contenedor puntaje escalado
ancho_cont_puntaje = pantalla.get_width() * 0.18
alto_cont_puntaje = pantalla.get_height() * 0.12
img_cont_puntaje = colocar_img_boton(RUTA_CONT_PUNTAJE, ancho_cont_puntaje, alto_cont_puntaje)

# Creacion del rectangulo contenedor
# El rectángulo contenedor ocupa 60% del ancho de pantalla y 90% del alto,
# y está desplazado 30% desde la izquierda para quedar centrado.
rect_contenedor_y = int(pantalla.get_height() * 0.05)        # 5% de margen
rect_contenedor_x = int(pantalla.get_width() * 0.30)         # 30% desde la izquierda
rect_contenedor_ancho = int(pantalla.get_width() * 0.60)     # 60% del ancho total
rect_contenedor_alto  = int(pantalla.get_height() * 0.90)    # 90% del alto total
rect_contenedor = pygame.Rect(
    rect_contenedor_x,
    rect_contenedor_y,
    rect_contenedor_ancho,
    rect_contenedor_alto
)

# Diccionario de elementos del tablero
elementos_tablero = {
    "oreo": {
        "img": "ruta",
        "puntos": 20
    },
    "bonobon": {
        "img": "ruta",
        "puntos": 15
    },
    "chupetin": {
        "img": "ruta",
        "puntos": 10
    },
    "chicle": {
        "ruta": "ruta",
        "puntaje": 8
    },
    "caramelo": {
        "ruta": "ruta",
        "puntaje": 5
    },
    "mantecol": {
        "ruta": "ruta",
        "puntaje": 12
    } 
}


# Creacion de la matriz 
generar_tablero_valido_match_3(CANTIDAD_FILAS, CANTIDAD_COLUMNAS, elementos_tablero, rect_contenedor)

# Variables de estado del bucle
pantalla_actual = "principal"
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        # Cierra la ventana si se da a la cruz
        if evento.type == pygame.QUIT:
            corriendo = False

        # Manejo de eventos por pantalla
        if pantalla_actual == "principal":
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_boton_jugar.collidepoint(evento.pos):
                    # Si se entra a la pantalla juego, se genera la matriz valida
                    matriz = generar_tablero_valido_match_3(CANTIDAD_FILAS, CANTIDAD_COLUMNAS, elementos_tablero, rect_contenedor)
                    puntaje = 0
                    pantalla_actual = "juego"

                    # Se ingresa a la pantalla de puntajes
                elif rect_boton_puntaje.collidepoint(evento.pos):
                    pantalla_actual = "puntajes"

                    # Cambia a la siguiente resolucion y acopla todos los elementos a ella
                elif rect_boton_resolucion.collidepoint(evento.pos):
                    indice_resolucion = (indice_resolucion + 1) % len(RESOLUCIONES)
                    pantalla = pygame.display.set_mode(RESOLUCIONES[indice_resolucion])

                    # Reescalado de fondos
                    tam_actual_pantalla = pantalla.get_size()  # Tupla (ancho, alto)
                    FONDO_PANTALLA_PRINCIPAL = escalar_fondo(RUTA_FONDO_PRINCIPAL, tam_actual_pantalla)
                    FONDO_PUNTAJES = escalar_fondo(RUTA_FONDO_PUNTAJES, tam_actual_pantalla)
                    FONDO_JUEGO = escalar_fondo(RUTA_FONDO_JUEGO, tam_actual_pantalla)
                    FONDO_REGISTRO = escalar_fondo(RUTA_FONDO_REGISTRO, tam_actual_pantalla)

                    # Reescalado de botones
                    ancho_boton = pantalla.get_width() * 0.20  # Los botones ocupan el 20% del ancho de pantalla
                    alto_boton = pantalla.get_height() * 0.08  # Los botones ocupan el 8% del alto de pantalla
                    x_boton = (pantalla.get_width() / 2) - (ancho_boton / 2)  # Centrado horizontal

                    y_boton_jugar      = pantalla.get_height() * 0.45  # 45% desde arriba para el botón "Jugar"
                    y_boton_puntaje    = pantalla.get_height() * 0.60  # 60% desde arriba para "Puntajes"
                    y_boton_resolucion = pantalla.get_height() * 0.75  # 75% para "Resolución"
                    y_boton_salir      = pantalla.get_height() * 0.90  # 90% para "Salir"

                    rect_boton_jugar      = pygame.Rect(x_boton, y_boton_jugar, ancho_boton, alto_boton)
                    rect_boton_puntaje    = pygame.Rect(x_boton, y_boton_puntaje, ancho_boton, alto_boton)
                    rect_boton_resolucion = pygame.Rect(x_boton, y_boton_resolucion, ancho_boton, alto_boton)
                    rect_boton_salir      = pygame.Rect(x_boton, y_boton_salir, ancho_boton, alto_boton)
                    rect_boton_volver     = pygame.Rect(x_boton, y_boton_salir, ancho_boton, alto_boton) 
                    rect_boton_reiniciar  = pygame.Rect(x_boton, y_boton_salir, ancho_boton, alto_boton)

                    # Reescalado de imagenes
                    img_btn_jugar      = colocar_img_boton(RUTA_JUGAR_BTN, ancho_boton, alto_boton)
                    img_btn_puntajes   = colocar_img_boton(RUTA_PUNTAJES_BTN, ancho_boton, alto_boton)
                    img_btn_resolucion = colocar_img_boton(RUTA_RESOLUCION_BTN, ancho_boton, alto_boton)
                    img_btn_salir      = colocar_img_boton(RUTA_SALIR_BTN, ancho_boton, alto_boton)
                    img_btn_volver     = colocar_img_boton(RUTA_VOLVER_BTN, ancho_boton, alto_boton)
                    img_btn_reiniciar  = colocar_img_boton(RUTA_REINICIAR_BTN, ancho_boton, alto_boton)

                    rect_img_jugar      = img_btn_jugar.get_rect(center=rect_boton_jugar.center)
                    rect_img_puntajes   = img_btn_puntajes.get_rect(center=rect_boton_puntaje.center)
                    rect_img_resolucion = img_btn_resolucion.get_rect(center=rect_boton_resolucion.center)
                    rect_img_salir      = img_btn_salir.get_rect(center=rect_boton_salir.center)
                    rect_img_volver     = img_btn_volver.get_rect(center=rect_boton_volver.center)
                    rect_img_reiniciar    = img_btn_reiniciar.get_rect(center=rect_boton_reiniciar.center)

                    # Timer reescalado
                    ancho_timer = pantalla.get_width() * 0.18
                    alto_timer = pantalla.get_height() * 0.12
                    img_timer = colocar_img_boton(RUTA_TIMER_BTN, ancho_timer, alto_timer)

                    # Contenedor puntaje reescalado
                    ancho_cont_puntaje = pantalla.get_width() * 0.18
                    alto_cont_puntaje = pantalla.get_height() * 0.12
                    img_cont_puntaje = colocar_img_boton(RUTA_CONT_PUNTAJE, ancho_cont_puntaje, alto_cont_puntaje)

                    # Reescalado de rectangulo contenedor
                    rect_contenedor_y = int(pantalla.get_height() * 0.05)        # 5% de margen
                    rect_contenedor_x = int(pantalla.get_width() * 0.30)         # 30% desde la izquierda
                    rect_contenedor_ancho = int(pantalla.get_width() * 0.60)     # 60% del ancho total
                    rect_contenedor_alto  = int(pantalla.get_height() * 0.90)    # 90% del alto total
                    rect_contenedor = pygame.Rect(
                        rect_contenedor_x,
                        rect_contenedor_y,
                        rect_contenedor_ancho,
                        rect_contenedor_alto
                    )

                    # Si se clickea en salir se cierra le juego
                elif rect_boton_salir.collidepoint(evento.pos):
                    corriendo = False


