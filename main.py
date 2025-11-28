import pygame
from modulos.constantes import *
from modulos.funciones import *

# Inicialización de la pantalla principal
pygame.init()
pygame.display.set_icon(LOGO)  # Carga el icono de la ventana 
pygame.display.set_caption(TITULO_JUEGO) # Titulo de la pantalla principal

# Pantalla y resolucion
indice_resolucion = 0  
pantalla = pygame.display.set_mode(RESOLUCIONES[indice_resolucion])  # Se crea la pantalla con la resolucion inicial
ancho_base = RESOLUCIONES[indice_resolucion][0]
ancho_actual = pantalla.get_width()
factor = ancho_actual / ancho_base

# Musica del juego
musica_menu = pygame.mixer.music.load(SONIDO_MENU)
sonido_vic = pygame.mixer.Sound(SONIDO_VICTORIA)
sonido_comodin = pygame.mixer.Sound(SONIDO_COMODIN)

pygame.mixer.music.set_volume(VOL_MUSICA)  # El volumen de la musica
pygame.mixer.music.play(-1)    # Se reproduce la música en loop infinito.

# Fuentes
fuente_timer = pygame.font.SysFont("holly berry pop", int(80 * factor))                
fuente_titulo = pygame.font.SysFont("holly berry pop", int(100 * factor), True, True)  
fuente_puntaje = pygame.font.SysFont("holly berry pop", int(25 * factor))              
fuente_input = pygame.font.SysFont("holly berry pop", int(60 * factor))     
fuente_puntaje_registro = pygame.font.SysFont("holly berry pop", int(55 * factor))      

# Carga y escalado de fondos para que se ajusten a la pantalla actual
tam_actual_pantalla = pantalla.get_size()  # Devuelve una tupla (ancho, alto)
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
y_boton_jugar = pantalla.get_height() * 0.45  # 45% desde arriba para el botón "Jugar"
y_boton_puntaje = pantalla.get_height() * 0.60  # 60% desde arriba para "Puntajes"
y_boton_resolucion = pantalla.get_height() * 0.75  # 75% para "Resolución"
y_boton_salir = pantalla.get_height() * 0.90  # 90% para "Salir"
y_boton_volver = pantalla.get_height() - alto_boton - int(pantalla.get_height()*0.03) # Esquina inferior izquierda
y_boton_reiniciar = y_boton_volver - alto_boton - int(pantalla.get_height()*0.02) # Encima de volver

# Parámetros para ranuras
ancho_ranura = int(pantalla.get_width() * 0.35)
alto_ranura = int(pantalla.get_height() * 0.05)
x_ranura = (pantalla.get_width() - ancho_ranura) // 2
margen_superior_ranura = int(pantalla.get_height() * 0.40)  # Abajo de "MEJORES PUNTAJES"
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
rect_contenedor_y = int(pantalla.get_height() * 0.09)        # 9% de margen
rect_contenedor_x = int(pantalla.get_width() * 0.26)         # 26% desde la izquierda
rect_contenedor_ancho = int(pantalla.get_width() * 0.66)     # 66% del ancho total
rect_contenedor_alto  = int(pantalla.get_height() * 0.82)    # 82% del alto total
rect_contenedor = pygame.Rect(rect_contenedor_x, rect_contenedor_y, rect_contenedor_ancho, rect_contenedor_alto)

# Diccionario de elementos del tablero
elementos_tablero = {
    "oreo": {"tipo": "oreo", "img": "assets/img/oreobon.png", "puntos": 20},
    "bonobon": {"tipo": "bonobon", "img": "assets/img/bon_o_bon.png", "puntos": 15},
    "chupetin": {"tipo": "chupetin", "img": "assets/img/chupetin.png", "puntos": 10},
    "bubbaloo": {"tipo": "bubbaloo", "img": "assets/img/bubbaloo.png", "puntos": 8},
    "flinpaf": {"tipo": "flinpaf", "img": "assets/img/flinpaf.png", "puntos": 5},
    "mantecol": {"tipo": "mantecol", "img": "assets/img/mantecol.png", "puntos": 12} 
}

comodin_tablero = {
    "comodin": {"tipo": "comodin", "img": "assets/img/comodin.png", "puntos": 50}
} 

# Lista de ranuras
imagenes_ranura = [RANURA_1ERO, RANURA_2DO, RANURA_3ERO] + [RANURA_NORMAL] * 7

# Evento timer
TIMER_EVENTO = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENTO, 1000)

# Variables de estado del bucle
pantalla_actual = "principal"
nombre_usuario = ""
corriendo = True
lista_puntajes = cargar_lista_puntajes() 

# Variables de control y logica del juego
celda_seleccionada = None
estado_juego = "jugando" 
tiempo_ultimo_cambio = 0
TIEMPO_ESPERA = 800 # Delay de 800ms

while corriendo:
    # Se guarda el tiempo actual
    tiempo_actual = pygame.time.get_ticks()

    # Logica de delay 
    if estado_juego == "esperando_borrar":
        if tiempo_actual - tiempo_ultimo_cambio > TIEMPO_ESPERA:
            # Se la limpieza y suma los puntos
            pts_extra = eliminar_y_puntuar(matriz, elementos_tablero, comodin_tablero)
            puntaje += pts_extra
            
            # Cambiar estado y se muestrabn las celdas vacias
            estado_juego = "esperando_rellenar"
            tiempo_ultimo_cambio = tiempo_actual 

    elif estado_juego == "esperando_rellenar":
        if tiempo_actual - tiempo_ultimo_cambio > TIEMPO_ESPERA:
            # Rellena con nuevos caramelos
            rellenar_tablero(matriz, elementos_tablero)
            
            # Se marcan los matches para eliminar
            if marcar_matches(matriz, SONIDO_COMODIN, SONIDO_COMBO):
                estado_juego = "esperando_borrar"
                tiempo_ultimo_cambio = tiempo_actual
            else:
                estado_juego = "jugando"

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        # Manejo de evento del timer
        elif evento.type == TIMER_EVENTO:
            if pantalla_actual == "juego":
                if tiempo_timer > 0:
                    tiempo_timer -= 1
                else:   # Cuando el timer llega a 0
                    pygame.mixer.music.stop()   # Pongo en stop la musica de fond
                    sonido_vic.set_volume(VOL_MUSICA)
                    reproducir_sonido(SONIDO_VICTORIA)
                    nombre_usuario = ""
                    pantalla_actual = "fin del juego"

        # 3. Manejo del teclado 
        elif evento.type == pygame.KEYDOWN:
            if pantalla_actual == "fin del juego":
                if evento.key == pygame.K_BACKSPACE:
                    nombre_usuario = nombre_usuario[:-1]  # Borra el último caracter
                elif evento.key == pygame.K_RETURN:
                    # Si se toca enter se guarda y sale
                    if len(nombre_usuario) > 0:
                        with open("puntajes.csv", "a") as archivo:
                            archivo.write(f"{nombre_usuario},{puntaje}\n")
                        lista_puntajes = cargar_lista_puntajes()
                        pantalla_actual = "principal"
                        pygame.mixer.music.play(-1)
                else:
                    # Si no es borrar ni enter
                    if len(nombre_usuario) < 12 and evento.unicode.isprintable():
                        nombre_usuario += evento.unicode

        # Manejo de eventos por pantalla
        elif evento.type == pygame.MOUSEBUTTONDOWN:

            # Eventos menu principal
            if pantalla_actual == "principal":
                if rect_boton_jugar.collidepoint(evento.pos):
                    reproducir_sonido(SONIDO_CLICK)
                    matriz = generar_tablero_valido_match_3(CANTIDAD_FILAS, CANTIDAD_COLUMNAS, elementos_tablero, rect_contenedor)
                    puntaje = 0
                    tiempo_timer = DURACION_TIMER
                    pantalla_actual = "juego"
                
                elif rect_boton_puntaje.collidepoint(evento.pos):
                    reproducir_sonido(SONIDO_CLICK)
                    pantalla_actual = "puntajes"

                # Logica de cambio de resolucion (Reescalado)
                elif rect_boton_resolucion.collidepoint(evento.pos):
                    reproducir_sonido(SONIDO_CLICK)
                    indice_resolucion = (indice_resolucion + 1) % len(RESOLUCIONES)
                    pantalla = pygame.display.set_mode(RESOLUCIONES[indice_resolucion])

                    # Recalcula el factor con la nueva resolucion
                    ancho_base = RESOLUCIONES[indice_resolucion][0]
                    ancho_actual = pantalla.get_width()
                    factor = ancho_actual / ancho_base

                    # Reescalado de fondos
                    tam_actual_pantalla = pantalla.get_size()  # Tupla (ancho, alto)
                    FONDO_PANTALLA_PRINCIPAL = escalar_fondo(RUTA_FONDO_PRINCIPAL, tam_actual_pantalla)
                    FONDO_PUNTAJES = escalar_fondo(RUTA_FONDO_PUNTAJES, tam_actual_pantalla)
                    FONDO_JUEGO = escalar_fondo(RUTA_FONDO_JUEGO, tam_actual_pantalla)
                    FONDO_REGISTRO = escalar_fondo(RUTA_FONDO_REGISTRO, tam_actual_pantalla)

                    # Reescalado de fuentes 
                    fuente_timer = pygame.font.SysFont("holly berry pop", int(80 * factor))
                    fuente_titulo = pygame.font.SysFont("holly berry pop", int(100 * factor), True, True)
                    fuente_puntaje = pygame.font.SysFont("holly berry pop", int(25 * factor))
                    fuente_input = pygame.font.SysFont("holly berry pop", int(60 * factor))    
                    fuente_puntaje_registro = pygame.font.SysFont("holly berry pop", int(45 * factor)) 

                    # Reescalado de botones
                    ancho_boton = pantalla.get_width() * 0.20 
                    alto_boton = pantalla.get_height() * 0.08 
                    x_boton = (pantalla.get_width() / 2) - (ancho_boton / 2) 
                    margen_izquierdo = pantalla.get_width() * 0.04

                    y_boton_jugar      = pantalla.get_height() * 0.45
                    y_boton_puntaje    = pantalla.get_height() * 0.60
                    y_boton_resolucion = pantalla.get_height() * 0.75
                    y_boton_salir      = pantalla.get_height() * 0.90
                    y_boton_volver = pantalla.get_height() - alto_boton - int(pantalla.get_height()*0.03)
                    y_boton_reiniciar = y_boton_volver - alto_boton - int(pantalla.get_height()*0.02)

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
                    margen_superior_ranura = int(pantalla.get_height() * 0.40)
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

                    # Contenedor puntaje reescalado
                    ancho_cont_puntaje = pantalla.get_width() * 0.20
                    alto_cont_puntaje = pantalla.get_height() * 0.18
                    img_cont_puntaje = colocar_img_boton(RUTA_CONT_PUNTAJE, ancho_cont_puntaje, alto_cont_puntaje)
                    rect_img_cont_puntaje = img_cont_puntaje.get_rect(midleft=(margen_izquierdo, pantalla.get_height() // 2))

                    # Reescalado de rectangulo contenedor
                    rect_contenedor_y = int(pantalla.get_height() * 0.09)
                    rect_contenedor_x = int(pantalla.get_width() * 0.26)
                    rect_contenedor_ancho = int(pantalla.get_width() * 0.66)
                    rect_contenedor_alto  = int(pantalla.get_height() * 0.82)
                    rect_contenedor = pygame.Rect(rect_contenedor_x, rect_contenedor_y, rect_contenedor_ancho, rect_contenedor_alto)

                elif rect_boton_salir.collidepoint(evento.pos):
                    reproducir_sonido(SONIDO_CLICK)
                    corriendo = False

            # Eventos click puntajes
            elif pantalla_actual == "puntajes":
                if rect_boton_volver.collidepoint(evento.pos):
                    reproducir_sonido(SONIDO_CLICK)
                    pantalla_actual = "principal"

            # Eventos click juego
            elif pantalla_actual == "juego":
                # Solo te deja clickear mientras no haya animacion (delay)
                if estado_juego == "jugando":
                    if rect_boton_volver.collidepoint(evento.pos):
                        reproducir_sonido(SONIDO_CLICK)
                        pantalla_actual = "principal"
                    elif rect_boton_reiniciar.collidepoint(evento.pos):
                        reproducir_sonido(SONIDO_CLICK)
                        matriz = generar_tablero_valido_match_3(CANTIDAD_FILAS, CANTIDAD_COLUMNAS, elementos_tablero, rect_contenedor)
                        puntaje = 0
                        tiempo_timer = DURACION_TIMER
                        celda_seleccionada = None
                        estado_juego = "jugando"
                    else:
                        # Click en el tablero (Swappeo)
                        ubicacion_click = obtener_coordenada_click(matriz, evento.pos)

                        if ubicacion_click != None:
                            if celda_seleccionada is None:
                                celda_seleccionada = ubicacion_click
                            else:
                                if son_vecinos(celda_seleccionada, ubicacion_click):
                                    # Swappea
                                    intercambiar(matriz, celda_seleccionada, ubicacion_click)
                                    
                                    # Marca los match
                                    if marcar_matches(matriz, SONIDO_COMODIN, SONIDO_COMBO, ubicacion_click):
                                        estado_juego = "esperando_borrar"
                                        tiempo_ultimo_cambio = pygame.time.get_ticks()
                                    else:
                                        intercambiar(matriz, celda_seleccionada, ubicacion_click)
                                    
                                    celda_seleccionada = None
                                else:
                                    celda_seleccionada = ubicacion_click

    # Render pantalla principal
    if pantalla_actual == "principal":
        pantalla.blit(FONDO_PANTALLA_PRINCIPAL, (0, 0))
        pantalla.blit(img_btn_jugar, rect_img_jugar)
        pantalla.blit(img_btn_puntajes, rect_img_puntajes)
        pantalla.blit(img_btn_resolucion, rect_img_resolucion)
        pantalla.blit(img_btn_salir, rect_img_salir)

    # Render pantalla puntajes
    elif pantalla_actual == "puntajes":
        pantalla.blit(FONDO_PUNTAJES, (0, 0))

        for i in range(len(imagenes_ranura)):
            y_ranura = margen_superior_ranura + i * (alto_ranura + margen_vertical_ranura)
            imagen_ranura_escalada = pygame.transform.scale(imagenes_ranura[i], (ancho_ranura, alto_ranura))
            rect_ranura = imagen_ranura_escalada.get_rect(topleft=(x_ranura, y_ranura))
            pantalla.blit(imagen_ranura_escalada, rect_ranura)

            if i < len(lista_puntajes):
                nombre, puntaje_p = lista_puntajes[i]
                ajuste_altura = int(alto_ranura * 0.22)
                pos_y_texto = y_ranura + ajuste_altura

                texto_nombre = fuente_puntaje.render(nombre, True, (NEGRO))
                texto_puntaje = fuente_puntaje.render(str(puntaje_p), True, (NEGRO))
                
                pantalla.blit(texto_nombre, (x_ranura + 30, pos_y_texto))
                pantalla.blit(texto_puntaje, (x_ranura + ancho_ranura - 80, pos_y_texto))

        pantalla.blit(img_btn_volver, rect_boton_volver)

    elif pantalla_actual == "juego":
        pantalla.blit(FONDO_JUEGO, (0, 0))
        pantalla.blit(img_btn_volver, rect_img_volver)
        pantalla.blit(img_btn_reiniciar, rect_img_reiniciar)

        # Contenedor puntaje
        pantalla.blit(img_cont_puntaje, rect_img_cont_puntaje)
        texto_puntaje = fuente_puntaje_registro.render(str(puntaje), True, (65,35,30))
        # Recalcula el centro
        rect_puntaje_display = texto_puntaje.get_rect(center=rect_img_cont_puntaje.center)
        pantalla.blit(texto_puntaje, rect_puntaje_display)

        # Timer
        pantalla.blit(img_timer, rect_img_timer)
        texto_timer = fuente_timer.render(str(tiempo_timer), True, (65,35,30))
        rect_timer_display = texto_timer.get_rect(center=rect_img_timer.center)
        pantalla.blit(texto_timer, rect_timer_display)

        # Tablero
        FONDO_TABLERO = escalar_fondo(RUTA_FONDO_TABLERO, (rect_contenedor.width, rect_contenedor.height))
        pantalla.blit(FONDO_TABLERO, rect_contenedor.topleft)
        dibujar_matriz(matriz, pantalla, celda_seleccionada)

    elif pantalla_actual == "fin del juego":
        pantalla.blit(FONDO_REGISTRO, (0, 0))

        # Nombre del usuario en la ranura
        centro_ranura_y = int(pantalla.get_height() * 0.38)
        COLOR_TEXTO_NOMBRE = (101, 67, 33)
        texto_nombre = fuente_input.render(nombre_usuario, True, NEGRO)
        rect_nombre = texto_nombre.get_rect(center=(pantalla.get_width() // 2, centro_ranura_y))
        pantalla.blit(texto_nombre, rect_nombre)

        # Puntaje abajo de la ranura
        centro_puntaje_y = int(pantalla.get_height() * 0.58)
        ancho_cont_puntaje = pantalla.get_width() * 0.30
        alto_cont_puntaje = pantalla.get_height() * 0.25

        img_puntaje_grande = colocar_img_boton(RUTA_CONT_PUNTAJE, ancho_cont_puntaje, alto_cont_puntaje)
        rect_img_puntaje = img_puntaje_grande.get_rect(center=(pantalla.get_width() // 2, centro_puntaje_y))
        pantalla.blit(img_puntaje_grande, rect_img_puntaje)

        # Textos del puntaje
        texto_titulo_puntaje = fuente_puntaje_registro.render(f"Puntaje", True, BLANCO)
        rect_titulo_puntaje = texto_titulo_puntaje.get_rect(center=rect_img_puntaje.center)
        rect_titulo_puntaje.y -= (alto_cont_puntaje * 0.15)
        pantalla.blit(texto_titulo_puntaje, rect_titulo_puntaje) 

        texto_puntaje_final = fuente_puntaje_registro.render(str(puntaje), True, BLANCO)
        rect_puntaje_final = texto_puntaje_final.get_rect(center=rect_img_puntaje.center)
        rect_puntaje_final.y += int(alto_cont_puntaje * 0.15)
        pantalla.blit(texto_puntaje_final, rect_puntaje_final)

    pygame.display.flip()
