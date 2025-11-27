import pygame
from modulos.constantes import *
from modulos.funciones import *

# Inicialización de la ventana principal
pygame.init()
pygame.display.set_icon(LOGO)  # Carga el icono de la ventana 
pygame.display.set_caption(TITULO_JUEGO) # Titulo de la ventana principal

# Pantalla y resolucion
indice_resolucion = 0  
pantalla = pygame.display.set_mode(RESOLUCIONES[indice_resolucion])  # Se crea la pantalla con la resolucion inicial

# Musica del juego
pygame.mixer.music.load(SONIDO_MENU)
pygame.mixer.music.set_volume(VOL_MUSICA)  # Se define el volumen de la musica
pygame.mixer.music.play(-1)    # Se reproduce la música en loop infinito.

# Fuentes
fuente_timer = pygame.font.SysFont("gabriola", 80)                # Fuente para timer.
fuente_titulo = pygame.font.SysFont("arial", 100, True, True)  # Fuente grande para títulos.
fuente_puntaje = pygame.font.SysFont("gabriola", 80)              # Fuente mediana para puntajes.
fuente_input = pygame.font.SysFont("gabriola", 60)                # Fuente para input de nombre de usuario.

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
margen_izquierdo = pantalla.get_width() * 0.04

# Posiciones verticales de botones
y_boton_jugar      = pantalla.get_height() * 0.45  # 45% desde arriba para el botón "Jugar"
y_boton_puntaje    = pantalla.get_height() * 0.60  # 60% desde arriba para "Puntajes"
y_boton_resolucion = pantalla.get_height() * 0.75  # 75% para "Resolución"
y_boton_salir      = pantalla.get_height() * 0.90  # 90% para "Salir"
y_boton_volver = pantalla.get_height() - alto_boton - int(pantalla.get_height()*0.03) # Esquina inferior izquierda
y_boton_reiniciar = y_boton_volver - alto_boton - int(pantalla.get_height()*0.02) # Encima de volver

# Parámetros para ranuras
ancho_ranura = int(pantalla.get_width() * 0.35)
alto_ranura = int(pantalla.get_height() * 0.05)
x_ranura = (pantalla.get_width() - ancho_ranura) // 2
margen_superior_ranura = int(pantalla.get_height() * 0.43)  # Justo debajo de "MEJORES PUNTAJES"
margen_vertical_ranura = int(alto_ranura * 0.13)

# Creacion de los rectángulos para cada botón
rect_boton_jugar      = pygame.Rect(x_boton, y_boton_jugar, ancho_boton, alto_boton)
rect_boton_puntaje    = pygame.Rect(x_boton, y_boton_puntaje, ancho_boton, alto_boton)
rect_boton_resolucion = pygame.Rect(x_boton, y_boton_resolucion, ancho_boton, alto_boton)
rect_boton_salir      = pygame.Rect(x_boton, y_boton_salir, ancho_boton, alto_boton)
rect_boton_reiniciar  = pygame.Rect(margen_izquierdo, y_boton_reiniciar, ancho_boton, alto_boton)
rect_boton_volver     = pygame.Rect(margen_izquierdo, y_boton_volver, ancho_boton, alto_boton) 

# Carga de las imágenes de los botones, escalándolas al tamanio de los botones
img_btn_jugar      = colocar_img_boton(RUTA_JUGAR_BTN, ancho_boton, alto_boton)
img_btn_puntajes   = colocar_img_boton(RUTA_PUNTAJES_BTN, ancho_boton, alto_boton)
img_btn_resolucion = colocar_img_boton(RUTA_RESOLUCION_BTN, ancho_boton, alto_boton)
img_btn_salir      = colocar_img_boton(RUTA_SALIR_BTN, ancho_boton, alto_boton)
img_btn_volver     = colocar_img_boton(RUTA_VOLVER_BTN, ancho_boton, alto_boton)
img_btn_reiniciar  = colocar_img_boton(RUTA_REINICIAR_BTN, ancho_boton, alto_boton)

# Timer escalado
ancho_timer = pantalla.get_width() * 0.20
alto_timer = pantalla.get_height() * 0.18
img_timer = colocar_img_boton(RUTA_TIMER_BTN, ancho_timer, alto_timer)

# Contenedor puntaje escalado
ancho_cont_puntaje = pantalla.get_width() * 0.20
alto_cont_puntaje = pantalla.get_height() * 0.18
img_cont_puntaje = colocar_img_boton(RUTA_CONT_PUNTAJE, ancho_cont_puntaje, alto_cont_puntaje)

# Centra las imágenes dentro de sus respectivos botones
rect_img_jugar = img_btn_jugar.get_rect(center=rect_boton_jugar.center)
rect_img_puntajes = img_btn_puntajes.get_rect(center=rect_boton_puntaje.center)
rect_img_resolucion = img_btn_resolucion.get_rect(center=rect_boton_resolucion.center)
rect_img_salir = img_btn_salir.get_rect(center=rect_boton_salir.center)
rect_img_volver = img_btn_volver.get_rect(center=rect_boton_volver.center)
rect_img_reiniciar = img_btn_reiniciar.get_rect(center=rect_boton_reiniciar.center)
rect_img_timer = img_timer.get_rect(topleft=(margen_izquierdo, int(pantalla.get_height()*0.04)))
rect_img_cont_puntaje = img_cont_puntaje.get_rect(midleft=(margen_izquierdo, pantalla.get_height() // 2))


# Creacion del rectangulo contenedor
# El rectángulo contenedor ocupa 60% del ancho de pantalla y 90% del alto,
# y está desplazado 30% desde la izquierda para quedar centrado.
rect_contenedor_y = int(pantalla.get_height() * 0.09)        # 5% de margen
rect_contenedor_x = int(pantalla.get_width() * 0.26)         # 30% desde la izquierda
rect_contenedor_ancho = int(pantalla.get_width() * 0.66)     # 72% del ancho total
rect_contenedor_alto  = int(pantalla.get_height() * 0.82)    # 88% del alto total
rect_contenedor = pygame.Rect(
    rect_contenedor_x,
    rect_contenedor_y,
    rect_contenedor_ancho,
    rect_contenedor_alto
)

# Diccionario de elementos del tablero
elementos_tablero = {
    "oreo": {
        "img": "assets\img\oreobon.png",
        "puntos": 20
    },
    "bonobon": {
        "img": "assets/img/bon_o_bon.png",
        "puntos": 15
    },
    "chupetin": {
        "img": "assets\img\chupetin.png",
        "puntos": 10
    },
    "bubbaloo": {
        "img": "assets/img/bubbaloo.png",
        "puntos": 8
    },
    "flinpaf": {
        "img": "assets/img/flinpaf.png",
        "puntos": 5
    },
    "mantecol": {
        "img": "assets\img\mantecol.png",
        "puntos": 12
    } 
}

comodin_tablero = {
    "comodin": {
        "img": "assets\img\comodin.png",
        "puntos": 50
    }
} 

# Lista de ranuras
imagenes_ranura = [RANURA_1ERO, RANURA_2DO, RANURA_3ERO] + [RANURA_NORMAL]*7

# Variables de estado del bucle
pantalla_actual = "principal"
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        # Cierra la ventana si se da a la cruz
        if evento.type == pygame.QUIT:
            corriendo = False

        # Manejo de eventos por pantalla
        if evento.type == pygame.MOUSEBUTTONDOWN:

                # Eventos menu principal
            if pantalla_actual == "principal":
                if rect_boton_jugar.collidepoint(evento.pos):
                    # Si se entra a la pantalla juego, se genera la matriz valida
                    matriz = generar_tablero_valido_match_3(CANTIDAD_FILAS, CANTIDAD_COLUMNAS, elementos_tablero, rect_contenedor)
                    puntaje = 0
                    tiempo_timer = DURACION_TIMER
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
                    margen_izquierdo = pantalla.get_width() * 0.04

                    y_boton_jugar      = pantalla.get_height() * 0.45  # 45% desde arriba para el botón "Jugar"
                    y_boton_puntaje    = pantalla.get_height() * 0.60  # 60% desde arriba para "Puntajes"
                    y_boton_resolucion = pantalla.get_height() * 0.75  # 75% para "Resolución"
                    y_boton_salir      = pantalla.get_height() * 0.90  # 90% para "Salir"
                    y_boton_volver = pantalla.get_height() - alto_boton - int(pantalla.get_height()*0.03) # Esquina inferior izquierda
                    y_boton_reiniciar = y_boton_volver - alto_boton - int(pantalla.get_height()*0.02) # Encima de volver

                    # Timer reescalado
                    ancho_timer = pantalla.get_width() * 0.20
                    alto_timer = pantalla.get_height() * 0.18
                    img_timer = colocar_img_boton(RUTA_TIMER_BTN, ancho_timer, alto_timer)

                    rect_boton_jugar      = pygame.Rect(x_boton, y_boton_jugar, ancho_boton, alto_boton)
                    rect_boton_puntaje    = pygame.Rect(x_boton, y_boton_puntaje, ancho_boton, alto_boton)
                    rect_boton_resolucion = pygame.Rect(x_boton, y_boton_resolucion, ancho_boton, alto_boton)
                    rect_boton_salir      = pygame.Rect(x_boton, y_boton_salir, ancho_boton, alto_boton)
                    rect_boton_reiniciar  = pygame.Rect(margen_izquierdo, y_boton_reiniciar, ancho_boton, alto_boton)
                    rect_boton_volver     = pygame.Rect(margen_izquierdo, y_boton_volver, ancho_boton, alto_boton) 

                    # Reescalado de ranuras
                    ancho_ranura = int(pantalla.get_width() * 0.35)
                    alto_ranura = int(pantalla.get_height() * 0.05)
                    x_ranura = (pantalla.get_width() - ancho_ranura) // 2
                    margen_superior_ranura = int(pantalla.get_height() * 0.43)  # Justo debajo de "MEJORES PUNTAJES"
                    margen_vertical_ranura = int(alto_ranura * 0.13)

                    # Reescalado de imagenes
                    img_btn_jugar      = colocar_img_boton(RUTA_JUGAR_BTN, ancho_boton, alto_boton)
                    img_btn_puntajes   = colocar_img_boton(RUTA_PUNTAJES_BTN, ancho_boton, alto_boton)
                    img_btn_resolucion = colocar_img_boton(RUTA_RESOLUCION_BTN, ancho_boton, alto_boton)
                    img_btn_salir      = colocar_img_boton(RUTA_SALIR_BTN, ancho_boton, alto_boton)
                    img_btn_volver     = colocar_img_boton(RUTA_VOLVER_BTN, ancho_boton, alto_boton)
                    img_btn_reiniciar  = colocar_img_boton(RUTA_REINICIAR_BTN, ancho_boton, alto_boton)

                    rect_img_jugar = img_btn_jugar.get_rect(center=rect_boton_jugar.center)
                    rect_img_puntajes = img_btn_puntajes.get_rect(center=rect_boton_puntaje.center)
                    rect_img_resolucion = img_btn_resolucion.get_rect(center=rect_boton_resolucion.center)
                    rect_img_salir = img_btn_salir.get_rect(center=rect_boton_salir.center)
                    rect_img_volver = img_btn_volver.get_rect(center=rect_boton_volver.center)
                    rect_img_reiniciar = img_btn_reiniciar.get_rect(center=rect_boton_reiniciar.center)
                    rect_img_timer = img_timer.get_rect(topleft=(margen_izquierdo, int(pantalla.get_height()*0.04)))
                    rect_img_cont_puntaje = img_cont_puntaje.get_rect(midleft=(margen_izquierdo, pantalla.get_height() // 2))

                    # Contenedor puntaje reescalado
                    ancho_cont_puntaje = pantalla.get_width() * 0.20
                    alto_cont_puntaje = pantalla.get_height() * 0.18
                    img_cont_puntaje = colocar_img_boton(RUTA_CONT_PUNTAJE, ancho_cont_puntaje, alto_cont_puntaje)

                    # Reescalado de rectangulo contenedor
                    rect_contenedor_y = int(pantalla.get_height() * 0.09)        # 5% de margen
                    rect_contenedor_x = int(pantalla.get_width() * 0.26)         # 30% desde la izquierda
                    rect_contenedor_ancho = int(pantalla.get_width() * 0.66)     # 72% del ancho total
                    rect_contenedor_alto  = int(pantalla.get_height() * 0.82)    # 88% del alto total
                    rect_contenedor = pygame.Rect(
                        rect_contenedor_x,
                        rect_contenedor_y,
                        rect_contenedor_ancho,
                        rect_contenedor_alto
                    )

                    # Si se clickea en salir se cierra le juego
                elif rect_boton_salir.collidepoint(evento.pos):
                    corriendo = False

                # Eventos puntajes
            elif pantalla_actual == "puntajes":
                if rect_boton_volver.collidepoint(evento.pos):
                    pantalla_actual = "principal"

                # Eventos juego
            elif pantalla_actual == "juego":
                if rect_boton_volver.collidepoint(evento.pos):
                    pantalla_actual = "principal"
                elif rect_boton_reiniciar.collidepoint(evento.pos):
                    matriz = generar_tablero_valido_match_3(CANTIDAD_FILAS, CANTIDAD_COLUMNAS, elementos_tablero, rect_contenedor)
                    puntaje = 0
                    tiempo_timer = DURACION_TIMER

        # Render pantalla principal
    if pantalla_actual == "principal":
        # Render del fondo
        pantalla.blit(FONDO_PANTALLA_PRINCIPAL, (0, 0))

        # Render botones
        pantalla.blit(img_btn_jugar, rect_img_jugar)
        pantalla.blit(img_btn_puntajes, rect_img_puntajes)
        pantalla.blit(img_btn_resolucion, rect_img_resolucion)
        pantalla.blit(img_btn_salir, rect_img_salir)

          # Render pantalla puntajes
    elif pantalla_actual == "puntajes":
          # Render del fondo
          pantalla.blit(FONDO_PUNTAJES, (0, 0))

# ------- RECORRE TODAS LAS RANURAS QUE HAY EN LA LISTA --------
          for i in range(len(imagenes_ranura)):
            # Calcula la posición vertical YY (uno debajo del otro, con margen)
            y_ranura = margen_superior_ranura + i * (alto_ranura + margen_vertical_ranura)

            # Escala la imagen al tamaño definido (así todas ocupan mismo ancho/alto)
            imagen_ranura_escalada = pygame.transform.scale(imagenes_ranura[i], (ancho_ranura, alto_ranura))
            rect_ranura = imagen_ranura_escalada.get_rect(topleft=(x_ranura, y_ranura))
            pantalla.blit(imagen_ranura_escalada, rect_ranura)

              # Si tenés datos para ese puesto (nombre y puntaje), dibujalos dentro de la ranura
            # if i < len(lista_puntajes):
            #      nombre, puntaje = lista_puntajes[i]  # Por ejemplo: ("Nacho", 330)
            #      texto_nombre = fuente_puntaje.render(nombre, True, (65,35,30))
            #      texto_puntaje = fuente_puntaje.render(str(puntaje), True, (65,35,30))
            #      # Nombre alineado a la izquierda
            #      pantalla.blit(texto_nombre, (x_ranura + 30, y_ranura + alto_ranura//3))
            #      # Puntaje alineado a la derecha
            #      pantalla.blit(texto_puntaje, (x_ranura + ancho_ranura - 80, y_ranura + alto_ranura//3))


          # Render botones
          pantalla.blit(img_btn_volver, rect_boton_volver)


    elif pantalla_actual == "juego":
        pantalla.blit(FONDO_JUEGO, (0, 0))

        # Botón volver
        pantalla.blit(img_btn_volver, rect_img_volver)

        # Botón reiniciar
        pantalla.blit(img_btn_reiniciar, rect_img_reiniciar)

        # Contenedor puntaje
        pantalla.blit(img_cont_puntaje, rect_img_cont_puntaje)
        texto_puntaje = fuente_puntaje.render(str(puntaje), True, (65,35,30))
        rect_puntaje_display = texto_puntaje.get_rect(center=rect_img_cont_puntaje.center)
        pantalla.blit(texto_puntaje, rect_puntaje_display)

        # Timer
        pantalla.blit(img_timer, rect_img_timer)
        texto_timer = fuente_timer.render(str(tiempo_timer), True, (65,35,30))
        rect_timer_display = texto_timer.get_rect(center=rect_img_timer.center)
        pantalla.blit(texto_timer, rect_timer_display)


        # Tablero del juego
        FONDO_TABLERO = escalar_fondo(RUTA_FONDO_TABLERO, (rect_contenedor.width, rect_contenedor.height))
        pantalla.blit(FONDO_TABLERO, rect_contenedor.topleft)
        dibujar_matriz(matriz, pantalla)

    pygame.display.flip()


