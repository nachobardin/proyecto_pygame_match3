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


# def dibujar_matriz(matriz: list[list], pantalla: pygame.Surface) -> None:
#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             # Escala la imagen al tamaño del rect; así respeta el layout adaptable
#             img_escalada = pygame.transform.scale(
#                 matriz[i][j]["img"], 
#                 (matriz[i][j]["rect"].width, matriz[i][j]["rect"].height)
#             )
#             pantalla.blit(img_escalada, matriz[i][j]["rect"])

# def son_vecinos(a: tuple, b: tuple) -> bool:
# #Devuelve True si las dos posiciones son adyacentes (arriba/abajo/izquierda/derecha)."""
#     r1, c1 = a
#     r2, c2 = b
#     return (abs(r1 - r2) == 1 and c1 == c2) or (abs(c1 - c2) == 1 and r1 == r2)




def buscar_matches(matriz: list[list]) -> set:
    """
    Busca coincidencias de 3 o más en filas y columnas.
    Devuelve un set con todas las posiciones que forman parte del match.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    celdas_matcheadas = set()

    # --- Buscar en filas ---
    for i in range(filas):
        contador = 1
        for j in range(1, columnas):
            if matriz[i][j]["tipo"] == matriz[i][j - 1]["tipo"]:
                contador += 1
            else:
                if contador >= 3:
                    for k in range(j - contador, j):
                        celdas_matcheadas.add((i, k))
                contador = 1

        if contador >= 3:
            for k in range(columnas - contador, columnas):
                celdas_matcheadas.add((i, k))

    # --- Buscar en columnas ---
    for j in range(columnas):
        contador = 1
        for i in range(1, filas):
            if matriz[i][j]["tipo"] == matriz[i - 1][j]["tipo"]:
                contador += 1
            else:
                if contador >= 3:
                    for k in range(i - contador, i):
                        celdas_matcheadas.add((k, j))
                contador = 1

        if contador >= 3:
            for k in range(filas - contador, filas):
                celdas_matcheadas.add((k, j))

    return celdas_matcheadas


def hay_match(matriz: list[list]) -> bool:
    """Devuelve True si existe un match de 3 o más en el tablero."""
    return len(buscar_matches(matriz)) > 0


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

def cargar_lista_puntajes():
    lista = []
    try:
        with open("puntajes.csv", "r") as archivo:
            for linea in archivo:
                try:
                    # Separa por la coma y limpia el salto de línea de una vez
                    nombre, puntaje = linea.strip().split(',')
                    # Agrega a la lista convirtiendo el puntaje a numero
                    lista.append((nombre, int(puntaje)))
                except ValueError:
                    # Si la linea está vacía o mal formada, la salta y sigue
                    continue
    except FileNotFoundError:
        return [] # Si no existe el archivo, devuelve lista vacía

    # Ordena de mayor a menor (tupla[1] es el puntaje)
    lista.sort(key=lambda tupla: tupla[1], reverse=True)
    
    return lista[:10]

def eliminar_y_rellenar(matriz, matches, elementos):
    """
    1. Calcula puntaje.
    2. Elimina items (pone None o genera nuevos).
    3. Retorna puntaje sumado.
    """
    puntos_ganados = 0
    
    # 1. Sumar puntos y "vaciar" celdas
    for (r, c) in matches:
        puntos_ganados += matriz[r][c]["puntos"]
        # Podríamos poner None, pero para hacerlo simple, generamos uno nuevo YA MISMO
        # y simulamos que "baja" después.
        # En un juego simple sin animación de caída compleja, podemos simplemente
        # reemplazar los matches por nuevos items directamentes.
        
    # Para hacerlo estilo Candy Crush (Gravedad):
    # Es un poco complejo de programar la caída exacta en una sola función simple.
    # VAMOS A HACER LA VERSIÓN SIMPLE: Reemplazar los eliminados por nuevos random.
    
    tipos = list(elementos.keys())
    
    for (r, c) in matches:
        nuevo_tipo = choice(tipos)
        datos = elementos[nuevo_tipo]
        
        # Guardamos el rect viejo para no perder la posición
        rect_viejo = matriz[r][c]["rect"]
        
        matriz[r][c] = {
            "tipo": nuevo_tipo,
            "puntos": datos["puntos"],
            "img": pygame.image.load(datos["img"]),
            "rect": rect_viejo # Mantenemos el rect
        }
        
    return puntos_ganados


def intercambiar(matriz: list[list], a: tuple, b: tuple) -> None:
    r1, c1 = a
    r2, c2 = b
    # Intercambio de datos (copia superficial)
    aux = matriz[r1][c1].copy()
    matriz[r1][c1] = matriz[r2][c2]
    matriz[r2][c2] = aux
    
    # Restaurar rects originales (física)
    temp_rect = matriz[r1][c1]["rect"]
    matriz[r1][c1]["rect"] = matriz[r2][c2]["rect"]
    matriz[r2][c2]["rect"] = temp_rect
    return None

def son_vecinos(a: tuple, b: tuple) -> bool:
    """
    Devuelve True si las celdas son adyacentes horizontal o verticalmente.
    NO incluye diagonales.
    """
    r1, c1 = a
    r2, c2 = b
    
    es_vecino = False
    
    # Chequeo horizontal (misma fila, columna difiere en 1)
    if r1 == r2:
        if c1 == c2 + 1 or c1 == c2 - 1:
            es_vecino = True
            
    # Chequeo vertical (misma columna, fila difiere en 1)
    elif c1 == c2:
        if r1 == r2 + 1 or r1 == r2 - 1:
            es_vecino = True
            
    return es_vecino


def marcar_matches(matriz: list[list]) -> bool:
    """
    METODO SIMPLIFICADO (Ventana Deslizante):
    Revisa grupos de 3 casilleros seguidos. Si son iguales, guarda sus coordenadas.
    """
    filas = len(matriz)
    cols = len(matriz[0])
    celdas_match = set() # Bolsa de coordenadas unicas
    
    # 1. BUSQUEDA HORIZONTAL
    # Vamos hasta 'cols - 2' porque miramos 2 casilleros adelante
    for f in range(filas):
        for c in range(cols - 2):
            tipo1 = matriz[f][c]["tipo"]
            tipo2 = matriz[f][c+1]["tipo"]
            tipo3 = matriz[f][c+2]["tipo"]
            
            # Si los 3 son iguales y NO son vacíos
            if tipo1 == tipo2 and tipo2 == tipo3 and tipo1 != "vacio":
                celdas_match.add((f, c))
                celdas_match.add((f, c+1))
                celdas_match.add((f, c+2))

    # 2. BUSQUEDA VERTICAL
    # Vamos hasta 'filas - 2' porque miramos 2 casilleros abajo
    for c in range(cols):
        for f in range(filas - 2):
            tipo1 = matriz[f][c]["tipo"]
            tipo2 = matriz[f+1][c]["tipo"]
            tipo3 = matriz[f+2][c]["tipo"]
            
            if tipo1 == tipo2 and tipo2 == tipo3 and tipo1 != "vacio":
                celdas_match.add((f, c))
                celdas_match.add((f+1, c))
                celdas_match.add((f+2, c))

    # 3. PROCESAR RESULTADOS (Comodines y Marcas)
    hay_match = False
    
    if len(celdas_match) > 0:
        hay_match = True
        
        # --- Paso A: Agrupar por color para ver si alguien junto 5 o mas ---
        grupos_por_color = {}
        
        for coord in celdas_match:
            f, c = coord
            color = matriz[f][c]["tipo"]
            
            # Si es la primera vez que vemos este color, creamos su lista
            if color in grupos_por_color:
                pass
            else:
                grupos_por_color[color] = []
            
            grupos_por_color[color].append(coord)
            
        # --- Paso B: Revisar quien merece comodin ---
        for color in grupos_por_color:
            lista_coords = grupos_por_color[color]
            
            # Si este grupo tiene 5 o mas celdas
            if len(lista_coords) >= 5:
                # Elegimos la primera celda para transformarla
                f_com, c_com = lista_coords[0]
                matriz[f_com][c_com]["efecto_comodin"] = True
                
                # Agregamos TODA la fila y columna a la bolsa de eliminar
                # (Esto es el poder del comodin activandose)
                for x in range(cols): 
                    celdas_match.add((f_com, x))
                for y in range(filas): 
                    celdas_match.add((y, c_com))

        # --- Paso C: Poner la etiqueta 'eliminar' final ---
        for coord in celdas_match:
            f, c = coord
            matriz[f][c]["eliminar"] = True

    return hay_match


def eliminar_y_puntuar(matriz: list[list], elementos: dict, comodin_dict: dict) -> int:
    """
    PROPOSITO:
        Recorre la matriz buscando celdas que fueron marcadas previamente por 'marcar_matches'.
        Ejecuta las acciones (eliminar o transformar) y calcula el puntaje total ganado.

    PARAMETROS:
        matriz: El tablero de juego.
        elementos: Diccionario con los caramelos normales.
        comodin_dict: Diccionario con la info del comodín.

    RETORNO:
        int: La cantidad total de puntos ganados en esta ronda.
    """
    
    # Inicializamos el contador de puntos de esta ronda en 0
    puntos_totales = 0
    
    filas = len(matriz)
    cols = len(matriz[0])
    
    # Recorremos celda por celda
    for f in range(filas):
        for c in range(cols):
            
            # Guardamos la celda actual en una variable corta para leer mejor
            celda = matriz[f][c]
            
            # --- CASO 1: EFECTO DE COMODIN ---
            # Si la celda fue elegida para convertirse en comodín (por un combo de 5)
            if celda.get("efecto_comodin") == True:
                
                # Sumamos el puntaje DEL COMODÍN (50)
                # (Adicional a su puntaje normal de caramelo que se suma abajo)
                puntos_totales += comodin_dict["comodin"]["puntos"]
                
                # Limpiamos la marca del efecto
                celda["efecto_comodin"] = False
                
            # 2. Eliminación (Esto pasa para todas las marcadas, incluida la del comodín)
            if celda.get("eliminar") == True:
                puntos_totales += celda["puntos"] # Puntos del caramelo normal (ej: 10)
                
                # Vaciamos
                celda["estado"] = "vacio"
                celda["tipo"] = "vacio"
                celda["img"] = None
                celda["eliminar"] = False

    return puntos_totales

def rellenar_tablero(matriz: list[list], elementos: dict) -> None:
    """
    PROPOSITO:
        Recorre toda la matriz buscando celdas que quedaron con estado "vacio".
        En esos lugares, genera un nuevo caramelo aleatorio para rellenar el hueco.
    
    PARAMETROS:
        matriz: El tablero de juego actual.
        elementos: El diccionario maestro (constantes) con la info de cada golosina (img, puntos).
    """
    
    filas = len(matriz)
    cols = len(matriz[0])
    
    # Obtenemos la lista de nombres posibles (ej: ['oreo', 'bonobon', ...])
    # Usamos keys() para tener solo los nombres.
    lista_elem_posibles = list(elementos.keys())
    
    # Recorremos cada casillero del tablero
    for f in range(filas):
        for c in range(cols):
            
            # Chequeamos si esta celda está vacía (hueco negro)
            if matriz[f][c].get("estado") == "vacio":
                
                # 1. ELEGIR QUÉ VAMOS A PONER
                # Elegimos un nombre al azar de la lista
                elem_nuevo = choice(lista_elem_posibles)
                
                # Buscamos los datos de ese nombre en el diccionario de constantes
                # (Acá sacamos cuánto vale y dónde está su imagen)
                datos_elem = elementos[elem_nuevo]
                
                # 2. RECUPERAR LA POSICIÓN (Clave para tu pregunta)
                # La celda vacía todavía tiene guardado su rectángulo (posición X, Y).
                # Lo guardamos en una variable para no perderlo al sobrescribir.
                rect_original = matriz[f][c]["rect"]
                
                # 3. CREAR EL NUEVO CARAMELO (INSTANCIA)
                # Creamos un diccionario nuevo con la mezcla de datos:
                # - Datos de la receta (tipo, puntos, imagen)
                # - Datos de la posición (rect)
                # - Datos de lógica (estado)
                matriz[f][c] = {
                    "tipo": elem_nuevo,                 # Nombre (ej: "oreo")
                    "puntos": datos_elem["puntos"],     # Valor (ej: 20)
                    "img": pygame.image.load(datos_elem["img"]), # Cargamos la imagen nueva
                    "rect": rect_original,                # ¡Acá reciclamos la posición vieja!
                    "estado": "activo"                    # Le avisamos al juego que este ya se puede usar
                }
                
    return None

def dibujar_matriz(matriz: list[list], pantalla: pygame.Surface, celda_sel: tuple = None) -> None:
    """
    PROPOSITO:
        Recorre cada celda del tablero lógico y dibuja su imagen correspondiente en la pantalla.
        Si hay una celda seleccionada (primer click), le dibuja un borde blanco para resaltar.
    
    PARAMETROS:
        matriz: La lista de listas que contiene los diccionarios de cada caramelo.
        pantalla: La superficie principal de Pygame donde vamos a 'pegar' (blit) las imágenes.
        celda_sel: (Opcional) Una tupla (fila, columna) indicando cuál caramelo clickeó el usuario.
                   Si es None, significa que no hay nada seleccionado.
    """
    
    filas = len(matriz)
    columnas = len(matriz[0])

    # Recorremos fila por fila (i)
    for i in range(filas):
        # Recorremos columna por columna (j)
        for j in range(columnas):
            
            # Guardamos el diccionario del caramelo actual en una variable corta
            elem = matriz[i][j]
            
            # --- 1. DIBUJO DEL CARAMELO ---
            # Solo dibujamos si la celda tiene una imagen válida.
            # Si item["img"] es None, significa que está "vacía" (ej: esperando caer),
            # así que no dibujamos nada (se verá el fondo del tablero).
            if elem.get("img") is not None:
                
                # Escalamos la imagen al tamaño exacto del rectángulo contenedor.
                # Esto es útil por si cambiaste la resolución o el tamaño de los rects.
                ancho_rect = elem["rect"].width
                alto_rect = elem["rect"].height
                img_escalada = pygame.transform.scale(elem["img"], (ancho_rect, alto_rect))
                
                # "Pegamos" la imagen escalada en la posición X,Y que dice el rect
                pantalla.blit(img_escalada, elem["rect"])
            
            # --- 2. DIBUJO DEL BORDE DE SELECCIÓN ---
            # Comparamos la coordenada actual (i, j) con la coordenada guardada en celda_sel
            if celda_sel == (i, j):
                # Si coinciden, dibujamos un cuadrado hueco encima
                # Parámetros: (superficie, color RGB blanco, rectángulo, grosor de línea)
                pygame.draw.rect(pantalla, (255, 255, 255), elem["rect"], 3)
                
    return None


def obtener_coordenada_click(matriz: list[list], pos_click: tuple) -> tuple:
    """
    Recibe la posición del mouse (x, y) y verifica si cayó sobre algún caramelo.
    Devuelve una tupla (fila, columna) si encontró algo, o None si clickeó afuera.
    """
    ubicacion_click = None
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            # Chequeamos si el rectángulo de la celda contiene al punto del click
            if matriz[i][j]["rect"].collidepoint(pos_click):
                ubicacion_click = (i, j)
                # Como ya encontramos, no hace falta seguir buscando.
                # (En una función, el return corta todo, así que es más eficiente)
                return ubicacion_click
                
    return ubicacion_click # Retorna None si recorrió todo y no encontró nada






