def calcular_botones(ancho_ventana, alto_ventana):
    ancho_boton = int(ancho_ventana * 0.3)
    alto_boton = int(alto_ventana * 0.07)
    margen_vertical = int(alto_ventana * 0.05)

    # Botones centrados horizontalmente
    x = (ancho_ventana - ancho_boton) // 2

    botones = {
        "jugar": pygame.Rect(x, margen_vertical + (alto_boton + margen_vertical) * 0, ancho_boton, alto_boton),
        "puntajes": pygame.Rect(x, margen_vertical + (alto_boton + margen_vertical) * 1, ancho_boton, alto_boton),
        "resolucion": pygame.Rect(x, margen_vertical + (alto_boton + margen_vertical) * 2, ancho_boton, alto_boton),
        "salir": pygame.Rect(x, margen_vertical + (alto_boton + margen_vertical) * 3, ancho_boton, alto_boton)
    }
    return botones