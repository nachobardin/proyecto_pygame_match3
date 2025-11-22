import pygame
import csv
from modulos.constantes import *
from modulos.funciones import *


# Inicialización y ventana
pygame.init()
pygame.display.set_icon(LOGO)
pantalla = pygame.display.set_mode(RESOLUCION_2)
pygame.display.set_caption(TITULO_JUEGO)


font = pygame.font.SysFont("arial", 30) # Fuente para el timer
# Inicializar musica
pygame.mixer.music.load(SONIDO_MENU)
pygame.mixer.music.set_volume(VOL_MUSICA)
pygame.mixer.music.play(-1)
# Fuentes
fuente = pygame.font.SysFont("arial", 100, True, True)
texto_pantalla = fuente.render("Pantalla Principal", True, COLOR_TEXTO_BOTON)
texto_pantalla_puntajes = fuente.render("Pantalla Puntajes", True, COLOR_TEXTO_BOTON)
# Posiciones de títulos
ubicacion_texto_x = (pantalla.get_width() / 2) - (texto_pantalla.get_width() / 2)
ubicacion_texto_y = pantalla.get_height() * 0.05
# Botones
ancho_boton = pantalla.get_width() * 0.20
alto_boton = pantalla.get_height() * 0.08
x_boton = (pantalla.get_width() / 2) - (ancho_boton / 2)
y_boton_jugar = pantalla.get_height() * 0.45
y_boton_puntaje = pantalla.get_height() * 0.60
y_boton_resolucion = pantalla.get_height() * 0.75
y_boton_salir = pantalla.get_height() * 0.90
# Rects botones
rect_boton_jugar = pygame.Rect(x_boton, y_boton_jugar, ancho_boton, alto_boton)
rect_boton_puntaje = pygame.Rect(x_boton, y_boton_puntaje, ancho_boton, alto_boton)
rect_boton_resolucion = pygame.Rect(x_boton, y_boton_resolucion, ancho_boton, alto_boton)
rect_boton_salir = pygame.Rect(x_boton, y_boton_salir, ancho_boton, alto_boton)
rect_boton_volver = pygame.Rect(x_boton, y_boton_salir, ancho_boton, alto_boton)
# Textos botones
def colocar_img_boton(ruta_img, x=400, y=235):
    boton = pygame.image.load(ruta_img)
    boton = pygame.transform.scale(boton, (x, y))
    return boton

# (400, 235) tamaño original de los botones
img_btn_jugar = colocar_img_boton(RUTA_JUGAR_BTN)
img_btn_puntajes = colocar_img_boton(RUTA_PUNTAJES_BTN)
img_btn_resolucion = colocar_img_boton(RUTA_RESOLUCION_BTN)
img_btn_salir = colocar_img_boton(RUTA_SALIR_BTN)
img_btn_volver = colocar_img_boton(RUTA_VOLVER_BTN)
img_timer = colocar_img_boton(RUTA_TIMER_BTN, x=900, y=300)
img_rectangulo = colocar_img_boton(RUTA_RECTANGULO, x=800, y=300)

rect_texto_jugar = img_btn_jugar.get_rect(center=rect_boton_jugar.center)
rect_texto_puntajes = img_btn_puntajes.get_rect(center=rect_boton_puntaje.center)
rect_texto_resolucion = img_btn_resolucion.get_rect(center=rect_boton_resolucion.center)
rect_texto_salir = img_btn_salir.get_rect(center=rect_boton_salir.center)
rect_texto_volver = img_btn_volver.get_rect(center=rect_boton_volver.center)
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
#Jugador
nombre_usuario = ""
ingresar_nombre = False

# Bucle principal
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        # Manejo de mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pantalla_actual == "principal": #Pantalla principal
                if rect_boton_jugar.collidepoint(evento.pos):
                    pantalla_actual = "juego"
                    start_time = pygame.time.get_ticks()  # Iniciar el temporizador al comenzar el juego
                elif rect_boton_puntaje.collidepoint(evento.pos):
                    pantalla_actual = "puntajes"
                elif rect_boton_resolucion.collidepoint(evento.pos):
                    pantalla_actual = "resolucion"
                elif rect_boton_salir.collidepoint(evento.pos):
                    corriendo = False
            elif pantalla_actual == "puntajes": # Pantalla puntajes
                if rect_boton_volver.collidepoint(evento.pos):
                    pantalla_actual = "principal"
            elif pantalla_actual == "resolucion": # Pantalla resolucion
                if rect_boton_volver.collidepoint(evento.pos):
                    pantalla_actual = "principal"
            elif pantalla_actual == "juego": # Pantalla juego
                if rect_boton_volver.collidepoint(evento.pos):
                    pantalla_actual = "principal"
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
        # Manejo de teclado para ingresar nombre en "Tiempo agotado"
        if pantalla_actual == "Tiempo agotado" and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                # Guardar el nombre en el archivo de puntajes
                with open("puntajes.csv", mode="a", newline="") as archivo:
                    escritor_csv = csv.writer(archivo)
                    escritor_csv.writerow([nombre_usuario])
                nombre_usuario = ""
                pantalla_actual = "principal"
            elif evento.key == pygame.K_BACKSPACE:
                nombre_usuario = nombre_usuario[:-1]
            elif len(nombre_usuario) < 10:
                nombre_usuario += evento.unicode
    if pantalla_actual == "principal":
        pantalla.blit(FONDO_PANTALLA_PRINCIPAL, (0, 0))
        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_jugar, border_radius=15)
        pantalla.blit(img_btn_jugar, rect_texto_jugar)
        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_puntaje, border_radius=15)
        pantalla.blit(img_btn_puntajes, rect_texto_puntajes)
        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_resolucion, border_radius=15)
        pantalla.blit(img_btn_resolucion, rect_texto_resolucion)
        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_salir, border_radius=15)
        pantalla.blit(img_btn_salir, rect_texto_salir)
    # PANTALLA PUNTAJES
    elif pantalla_actual == "puntajes":
        pantalla.blit(FONDO_PUNTAJES, (0, 0))
        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_volver, border_radius=15)
        pantalla.blit(img_btn_volver, rect_texto_volver)
        fuente_puntaje = pygame.font.SysFont("arial", 40)
        try:
            with open("puntajes.csv", newline="") as archivo:
                lector = csv.reader(archivo)
                for idx, fila in enumerate(lector):
                    nombre = fila[0]
                    puntaje = fila[1] if len(fila) > 1 else ""
                    texto = fuente_puntaje.render(f"{nombre} {puntaje}", True, (255, 255, 255))
                    pantalla.blit(texto, (100, 100 + idx * 50))  # Ajusta posición y espaciado
        except FileNotFoundError:
            texto = fuente_puntaje.render("No hay puntajes guardados.", True, (255, 255, 255))
            pantalla.blit(texto, (100, 100))
    # PANTALLA RESOLUCION
    elif pantalla_actual == "resolucion":
        pantalla.blit(FONDO_RESOLUCION, (0, 0))
        # pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_rectangulo, border_radius=15)
        # pantalla.blit(img_rectangulo, rect_rectangulo)
        pantalla.blit(img_btn_volver, rect_texto_volver)
    # PANTALLA JUEGO
    elif pantalla_actual == "juego":
        pantalla.blit(FONDO_JUEGO, (0, 0))
    
        rect_boton_volver = pygame.Rect(20, y_boton_salir, ancho_boton + 30, alto_boton)
        rect_texto_volver = img_btn_volver.get_rect(left=rect_boton_volver.left - 50, centery=rect_boton_volver.centery)
        pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton_volver, border_radius=15)
        pantalla.blit(img_btn_volver, rect_texto_volver)
        # --- Timer sobre imagen de reloj ---
        # Elige la posición donde quieres el reloj
        timer_x = 50
        timer_y = 50
        pantalla.blit(IMG_TIMER, (timer_x, timer_y))
        tiempo_restante = mostrar_timer_regresivo(pantalla, start_time, font, tiempo_total=5)
        # Renderiza el número del timer centrado sobre la imagen
        texto_timer = font.render(str(tiempo_restante), True, (255, 255, 255))
        rect_timer = IMG_TIMER.get_rect(topleft=(timer_x, timer_y))
        rect_texto = texto_timer.get_rect(center=rect_timer.center)
        pantalla.blit(texto_timer, rect_texto)
        if tiempo_restante == 0:
            print("Tiempo agotado. Fin del juego.")
            pygame.mixer.music.pause()
            pygame.mixer.Sound(SONIDO_VICTORIA).play()
            pantalla_actual = "Tiempo agotado"  # Volver a la pantalla principal o manejar el fin del juego
        # Marco del tablero
        pygame.draw.rect(pantalla, GRIS, rect_contenedor, border_radius=15)
        # Dibujar caramelos
        dibujar_matriz(matriz, pantalla)
        # Resaltar celda seleccionada
        if primer_click is not None:
            r, c = primer_click
            pygame.draw.rect(pantalla, ROJO, matriz[r][c]["rect"], 8, border_radius=5)
    
    #PANTALLA TIEMPO AGOTADO
    elif pantalla_actual == "Tiempo agotado":
        pantalla.blit(FONDO_REGISTRO, (0, 0))
        # Centrar el input box en la zona de escritura de la imagen
        input_box_width = 600
        input_box_height = 50
        input_box_x = int((pantalla.get_width() - input_box_width) // 2 + pantalla.get_width() * 0.05)
        input_box_y = int(pantalla.get_height() * 0.43)  # Zona de escritura
        
        input_box = pygame.Rect(input_box_x, input_box_y, input_box_width, input_box_height)
        
        #Cuadrado blanco del input box
        # pygame.draw.rect(pantalla, (255, 255, 255), input_box, border_radius=10)
        
        fuente_input = pygame.font.SysFont("arial", 40)
        texto_input = fuente_input.render(nombre_usuario, True, (0, 0, 0))
        pantalla.blit(texto_input, (input_box.x+10, input_box.y+10))
    pygame.display.flip()
pygame.quit()