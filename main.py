import pygame
from colores import *
from constantes import *

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
color_fondo = GRIS

pygame.display.set_caption("JuegoPY")

corriendo = True

while corriendo:
    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == pygame.QUIT: # Interaccion con la cruz de la ventana
            corriendo = False
    
    pantalla.fill(GRIS)

    pygame.display.flip()