import pygame
from colores import *
from constantes import *

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
color_fondo = GRIS

pygame.display.set_caption("JuegoPY")

corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Interaccion con la cruz de la ventana
            pygame.quit() # Cerramos la ventana de pygame
            quit()
    
    pantalla.fill(GRIS)

    pygame.display.flip()