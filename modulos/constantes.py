import pygame

# Tittulo del juego
TITULO_JUEGO = "Candy-Combo"

# Colores
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
GRIS = (128, 128, 128)
AMARILLO = (255, 255, 0)
CELESTE = ( 0, 0,128)
AZUL = ( 0, 0, 255)


# Resoluciones
RESOLUCIONES = [(1280, 720), (1024, 768), (800, 600)]

# Dimensiones del tablero
CANTIDAD_FILAS = 8
CANTIDAD_COLUMNAS = 8

# Colores aleatorios para botones
COLOR_TEXTO_BOTON = ROJO
COLOR_FONDO = GRIS


#Sonidos
SONIDO_MENU = "assets/audio/Candy Crush Saga OST - World Map.mp3"
VOL_MUSICA = 0.2
SONIDO_VICTORIA = "assets/audio/victoria.wav"

# Rutas imagenes
RUTA_LOGO = "assets/img/logo.png"
RUTA_FONDO_PRINCIPAL = "assets/img/fondo_imagen.jpg"
RUTA_FONDO_PUNTAJES = "assets/img/fondo_puntajes.png"
RUTA_FONDO_JUEGO = "assets/img/fondo_juego.png"
RUTA_FONDO_REGISTRO = "assets/img/fondo_registro.png"
RUTA_FONDO_RESOLUCION = "assets/img/fondo_resolucion.jpg"
RUTA_FONDO_TABLERO = "assets/img/fondo_tableroREC.png"

RUTA_JUGAR_BTN = "assets/img/boton_jugar.png"
RUTA_PUNTAJES_BTN = "assets/img/boton_puntajes.png"
RUTA_RESOLUCION_BTN = "assets/img/boton_resolucion.png"
RUTA_SALIR_BTN = "assets/img/boton_salir.png"
RUTA_VOLVER_BTN = "assets/img/boton_volver.png"
RUTA_REINICIAR_BTN = "assets/img/boton_reiniciar.png"

RUTA_TIMER_BTN = "assets/img/timer.png"
RUTA_CONT_PUNTAJE = "assets\img\contenedor_puntaje.png"

RUTA_FONDO_REGISTRO = "assets/img/fondo_registro.png"
RUTA_RECTANGULO = "assets/img/rectangulo.png"


# Imagenes cargadas
LOGO = pygame.image.load(RUTA_LOGO)
FONDO_PANTALLA_PRINCIPAL = pygame.image.load(RUTA_FONDO_PRINCIPAL)
FONDO_PANTALLA_PRINCIPAL = pygame.transform.scale(FONDO_PANTALLA_PRINCIPAL, RESOLUCIONES[0])


FONDO_PUNTAJES = pygame.image.load(RUTA_FONDO_PUNTAJES)
FONDO_PUNTAJES = pygame.transform.scale(FONDO_PUNTAJES, RESOLUCIONES[0])


FONDO_JUEGO = pygame.image.load(RUTA_FONDO_JUEGO)
FONDO_JUEGO = pygame.transform.scale(FONDO_JUEGO, RESOLUCIONES[0])


FONDO_REGISTRO = pygame.image.load(RUTA_FONDO_REGISTRO)
FONDO_REGISTRO = pygame.transform.scale(FONDO_REGISTRO, RESOLUCIONES[0])


FONDO_RESOLUCION = pygame.image.load(RUTA_FONDO_RESOLUCION)
FONDO_RESOLUCION = pygame.transform.scale(FONDO_RESOLUCION, RESOLUCIONES[0])

IMG_TIMER = pygame.image.load(RUTA_TIMER_BTN)
IMG_TIMER_ESCALADA = pygame.transform.scale(IMG_TIMER, (150, 90))
DURACION_TIMER = 60

RUTA_RANURA_1ERO = "assets/img/ranura1eroREC.png"
RUTA_RANURA_2DO =  "assets/img/ranura2doREC.png"
RUTA_RANURA_3ERO = "assets/img/ranura3eroREC.png"
RUTA_RANURA_NORMAL = "assets/img/ranuraNormalREC.png"

RANURA_1ERO = pygame.image.load(RUTA_RANURA_1ERO)
RANURA_2DO = pygame.image.load(RUTA_RANURA_2DO)
RANURA_3ERO = pygame.image.load(RUTA_RANURA_3ERO)
RANURA_NORMAL = pygame.image.load(RUTA_RANURA_NORMAL)