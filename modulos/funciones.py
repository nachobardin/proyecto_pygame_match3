import pygame
from random import *

def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial:any=None)->list[list]:
    """
    """
    matriz = []
    for _ in range(cant_filas):
        fila = []
        for _ in range(cant_columnas):
            fila.append(valor_inicial)
        matriz.append(fila)
    return matriz

# def cargar_matriz_elementos(matriz: list[list], elementos: dict) -> None:
#     """
#     Rellena la matriz, asignando en cada celda un diccionario con la imagen y el puntaje
#     de un caramelo aleatorio, usando los tipos definidos en 'elementos' (sin comodín).
#     La imagen se carga ahora (de la ruta correspondiente); el rect se asigna después.
#     """
#     tipos = list(elementos.keys())  # Lista de tipos de caramelos disponibles
#     for i in range(len(matriz)):           # Recorre cada fila
#         for j in range(len(matriz[i])):    # Recorre cada columna dentro de la fila
#             tipo = choice(tipos)           # Sortea el tipo para esta celda
#             datos = elementos[tipo]        # Saca puntaje y ruta de imagen
#             matriz[i][j] = {
#                 "puntos": datos["puntos"],                # Puntaje del caramelo sorteado
#                 "img": pygame.image.load(datos["img"])      # Imagen cargada, se escala después
#             }


def cargar_matriz_elementos(matriz: list[list], elementos: dict) -> None:
    tipos = list(elementos.keys()) # Lista de tipos de caramelos disponibles
    for i in range(len(matriz)):   # Recorre cada fila
        for j in range(len(matriz[i])):  # Recorre cada columna dentro de la fila
            tipo = choice(tipos)  # Sortea el tipo para esta celda
            datos = elementos[tipo] # Saca puntaje y ruta de imagen
            matriz[i][j] = {
                "tipo": tipo,
                "puntos": datos["puntos"],  # Puntaje del caramelo sorteado
                "img": pygame.image.load(datos["img"]) # Imagen cargada, se escala después
            }




def crear_botones_matriz_sobre_contenedor(matriz: list[list], rect_cont: pygame.Rect) -> None:
    """
    Asigna el campo "rect" a cada celda de la matriz, 
    calculando posición y tamaño para distribuir los caramelos dentro del área del tablero (`rect_cont`).
    Si cambia la resolución o el tamaño del tablero, hay que volver a llamar a esta función.
    """
    # Calcula ancho y alto para cada celda, dejando pequeños márgenes (4%)
    ancho_celda_matriz = int(rect_cont.width * 0.98 / len(matriz[0]))  # El 96% del ancho dividido "columnas"
    alto_celda_matriz  = int(rect_cont.height * 0.98 / len(matriz))    # El 96% del alto dividido "filas"
    # Offset para márgenes en el área del tablero ("dejamos 2% de marco arriba/izq")
    offset_x = int(rect_cont.width * 0.01) + rect_cont.x
    offset_y = int(rect_cont.height * 0.01) + rect_cont.y

    for i in range(len(matriz)):           # Para cada fila
        for j in range(len(matriz[i])):    # Para cada columna
            # Calcula el rectángulo donde se dibuja ese caramelo
            un_rectangulo = pygame.Rect(
                (j * ancho_celda_matriz) + offset_x,       # Posición x
                (i * alto_celda_matriz)  + offset_y,       # Posición y
                ancho_celda_matriz,                        # Ancho
                alto_celda_matriz                          # Alto
            )
            # Le agrega/actualiza el campo "rect" a la celda de la matriz
            matriz[i][j]["rect"] = un_rectangulo


def dibujar_matriz(matriz: list[list], pantalla: pygame.Surface) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            # Escala la imagen al tamaño del rect; así respeta el layout adaptable
            img_escalada = pygame.transform.scale(
                matriz[i][j]["img"], 
                (matriz[i][j]["rect"].width, matriz[i][j]["rect"].height)
            )
            pantalla.blit(img_escalada, matriz[i][j]["rect"])

def son_vecinos(a: tuple, b: tuple) -> bool:
#Devuelve True si las dos posiciones son adyacentes (arriba/abajo/izquierda/derecha)."""
    r1, c1 = a
    r2, c2 = b
    return (abs(r1 - r2) == 1 and c1 == c2) or (abs(c1 - c2) == 1 and r1 == r2)


def intercambiar(matriz: list[list], a: tuple, b: tuple) -> None:
    #Intercambia dos fichas de la matriz."""
    r1, c1 = a
    r2, c2 = b
    matriz[r1][c1]["color"], matriz[r2][c2]["color"] = matriz[r2][c2]["color"], matriz[r1][c1]["color"]


def buscar_matches(matriz: list[list]) -> set:
    """
    Busca coincidencias de 3 o más en filas y columnas.
    Devuelve un set con todas las posiciones que forman parte del match.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    celdas_en_match = set()

    # --- Buscar en filas ---
    for i in range(filas):
        contador = 1
        for j in range(1, columnas):
            if matriz[i][j]["color"] == matriz[i][j - 1]["color"]:
                contador += 1
            else:
                if contador >= 3:
                    for k in range(j - contador, j):
                        celdas_en_match.add((i, k))
                contador = 1

        if contador >= 3:
            for k in range(columnas - contador, columnas):
                celdas_en_match.add((i, k))

    # --- Buscar en columnas ---
    for j in range(columnas):
        contador = 1
        for i in range(1, filas):
            if matriz[i][j]["color"] == matriz[i - 1][j]["color"]:
                contador += 1
            else:
                if contador >= 3:
                    for k in range(i - contador, i):
                        celdas_en_match.add((k, j))
                contador = 1

        if contador >= 3:
            for k in range(filas - contador, filas):
                celdas_en_match.add((k, j))

    return celdas_en_match


def hay_match(matriz: list[list]) -> bool:
    """Devuelve True si existe un match de 3 o más en el tablero."""
    return len(buscar_matches(matriz)) > 0


# def mostrar_timer(screen, start_time, font, pos=(10, 10), color=(255, 255, 255)):
#     elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # segundos
#     timer_text = font.render(f"Tiempo: {elapsed_time}s", True, color)
#     screen.blit(timer_text, pos)


def mostrar_timer_regresivo(screen, start_time, font, tiempo_total=60, pos=(10, 10), color=(255, 255, 255)):
    lapso_tiempo = (pygame.time.get_ticks() - start_time) // 1000
    tiempo_restante = max(0, tiempo_total - lapso_tiempo)
    return tiempo_restante


def cambiar_resolucion(i, resoluciones):
    if i + 1 < len(resoluciones):
        nuevo_indice = i + 1
    else:
        nuevo_indice = 0
    nueva_resolucion = resoluciones[nuevo_indice]
    pantalla = pygame.display.set_mode(nueva_resolucion)
    return pantalla, nuevo_indice


def imagen_boton_escalada(ruta_img, rect):
    """
    """
    img = pygame.image.load(ruta_img)
    return pygame.transform.scale(img, (rect.width, rect.height))

def escalar_fondo(ruta, tamanio):
    """
    PROPOSITO: Carga una imagen de fondo y la escala al tamaño actual de la pantalla.
    """
    return pygame.transform.scale(pygame.image.load(ruta), tamanio)

def colocar_img_boton(ruta_img, ancho, alto):
    """
    PROPOSITO: Carga la imagen del botón desde archivo y la escala al tamaño recibido.
    """
    img = pygame.image.load(ruta_img)
    return pygame.transform.scale(img, (int(ancho), int(alto)))



def generar_tablero_valido_match_3(filas:int, columnas:int, elementos:dict, rect_cont) -> list[list]:
    """
    Sigue creando matrices aleatorias hasta que salga una que es válida.
    """
    while True:
        matriz = inicializar_matriz(filas, columnas, rect_cont)
        cargar_matriz_elementos(matriz, elementos)
        crear_botones_matriz_sobre_contenedor(matriz, rect_cont)
        if matriz_es_valida(matriz):
            return matriz
        
# def hay_match_resuelto(matriz: list[list]) -> bool:
#     """
#     Devuelve True si HAY algún grupo de 3 o más elementos iguales en fila o columna.
#     Se usa en la inicialización para rechazar matrices con combos ya hechos.
#     """
#     filas = len(matriz)
#     columnas = len(matriz[0])

#     # Chequeo filas
#     for i in range(filas):
#         for j in range(columnas - 2):  # Solo hasta la antepenúltima
#             tipo1 = matriz[i][j].get("img")
#             tipo2 = matriz[i][j+1].get("img")
#             tipo3 = matriz[i][j+2].get("img")
#             if tipo1 == tipo2 and tipo2 == tipo3:
#                 return True

#     # Chequeo columnas
#     for j in range(columnas):
#         for i in range(filas - 2):  # Solo hasta la antepenúltima
#             tipo1 = matriz[i][j].get("img")
#             tipo2 = matriz[i+1][j].get("img")
#             tipo3 = matriz[i+2][j].get("img")
#             if tipo1 == tipo2 and tipo2 == tipo3:
#                 return True

#     return False

def hay_match_resuelto(matriz: list[list]) -> bool:
    filas = len(matriz)
    columnas = len(matriz[0])
    # Chequeo filas
    for i in range(filas):
        for j in range(columnas - 2):  # Solo hasta la antepenúltima
            t1 = matriz[i][j]["tipo"]
            t2 = matriz[i][j+1]["tipo"]
            t3 = matriz[i][j+2]["tipo"]
            if t1 == t2 and t2 == t3:
                return True
    # Chequeo columnas
    for j in range(columnas):
        for i in range(filas - 2):  # Solo hasta la antepenúltima
            t1 = matriz[i][j]["tipo"]
            t2 = matriz[i+1][j]["tipo"]
            t3 = matriz[i+2][j]["tipo"]
            if t1 == t2 and t2 == t3:
                return True
    return False



# def hay_jugada_posible(matriz: list[list]) -> bool:
#     """
#     Devuelve True si existe algún swap entre dos adyacentes que forme un combo al hacerlo.
#     Así se garantiza que el tablero SIEMPRE tiene jugadas y no está bloqueado.
#     """
#     filas = len(matriz)
#     columnas = len(matriz[0])

#     for i in range(filas):
#         for j in range(columnas):
#             # Check hacia la derecha (swap horizontal)
#             if j < columnas - 1:
#                 matriz[i][j], matriz[i][j+1] = matriz[i][j+1], matriz[i][j]  # swap temporal
#                 if hay_match_resuelto(matriz):
#                     matriz[i][j], matriz[i][j+1] = matriz[i][j+1], matriz[i][j]  # revertir swap
#                     return True
#                 matriz[i][j], matriz[i][j+1] = matriz[i][j+1], matriz[i][j]  # revertir swap

#             # Check hacia abajo (swap vertical)
#             if i < filas - 1:
#                 matriz[i][j], matriz[i+1][j] = matriz[i+1][j], matriz[i][j]  # swap temporal
#                 if hay_match_resuelto(matriz):
#                     matriz[i][j], matriz[i+1][j] = matriz[i+1][j], matriz[i][j]  # revertir swap
#                     return True
#                 matriz[i][j], matriz[i+1][j] = matriz[i+1][j], matriz[i][j]  # revertir swap

#     return False

def hay_jugada_posible(matriz: list[list]) -> bool:
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            # Swap derecha
            if j < columnas - 1:
                matriz[i][j], matriz[i][j+1] = matriz[i][j+1], matriz[i][j]
                if hay_match_resuelto(matriz):
                    matriz[i][j], matriz[i][j+1] = matriz[i][j+1], matriz[i][j]
                    return True
                matriz[i][j], matriz[i][j+1] = matriz[i][j+1], matriz[i][j]
            # Swap abajo
            if i < filas - 1:
                matriz[i][j], matriz[i+1][j] = matriz[i+1][j], matriz[i][j]
                if hay_match_resuelto(matriz):
                    matriz[i][j], matriz[i+1][j] = matriz[i+1][j], matriz[i][j]
                    return True
                matriz[i][j], matriz[i+1][j] = matriz[i+1][j], matriz[i][j]
    return False


def matriz_es_valida(matriz: list[list]) -> bool:
    # No debe tener match hecho y debe tener jugada posible
    if hay_match_resuelto(matriz):
        return False
    if not hay_jugada_posible(matriz):
        return False
    return True

def mostrar_timer_regresivo(start_time, font, tiempo_total, pos=(10, 10), color=(255, 255, 255)):
    tiempo = tiempo_total
    lapso_tiempo = (pygame.time.get_ticks() - start_time) // 1000
    tiempo_restante = max(0, tiempo - lapso_tiempo)
    return tiempo_restante
