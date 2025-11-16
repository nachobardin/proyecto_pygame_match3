import pygame
from colores import *
from constantes import *
from funciones import *

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
color_fondo = GRIS

pygame.display.set_caption("JuegoPY")

#          BANDERAS   
pantalla_actual = "menu"
corriendo = True

#          BOTONES
botones = calcular_botones(ANCHO, ALTO)




while corriendo:
    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == pygame.QUIT: # Interaccion con la cruz de la ventana
            corriendo = False
    
    pantalla.fill(GRIS)

    pygame.display.flip()