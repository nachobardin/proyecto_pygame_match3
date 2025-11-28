import pygame
from random import choice

def inicializar_matriz(cant_filas: int, cant_columnas: int, valor_inicial: any = None) -> list[list]:
    """
    PROPOSITO: Crea una matriz con las dimensiones especificadas, inicializando cada celda con un None.

    PARAMETROS:
        * cant_filas: La cantidad de filas de la matriz.
        * cant_columnas: La cantidad de columnas de la matriz.
        * valor_inicial: Valor con el que se rellenan todas las celdas al principio.

    RETORNA: Una Matriz.
    """
    matriz = [] # Creamos la lista vacía que contendrá las filas
    
    # Iteramos filas
    for _ in range(cant_filas):
        fila = [] # Creamos una lista vacía para la fila actual
        
        # Iteramos columnas
        for _ in range(cant_columnas):
            fila.append(valor_inicial) # Agregamos el None
            
        matriz.append(fila) # Agregamos la fila completa a la matriz
    
    return matriz 


def cargar_matriz_elementos(matriz: list[list], elementos: dict) -> None:
    """
    PROPOSITO: Recorre la y rellena cada celda con un elemnto aleatorio del diccionario de elementos.

    PARAMETROS:
        * matriz: La matriz a rellenar.
        * elementos: Diccionario que tiene los datos de cada tipo de elemento.

    RETORNA: None.
    """
    # Obtenemos una lista con las claves (nombres) de los caramelos para poder elegir al azar
    tipos = list(elementos.keys()) 
    
    # Recorremos índice por índice las filas de la matriz
    for i in range(len(matriz)):
        # Recorremos índice por índice las columnas de la fila actual
        for j in range(len(matriz[i])):
            
            tipo = choice(tipos) # Elegimos un tipo de caramelo aleatorio
            datos = elementos[tipo] # Obtenemos los datos (img, puntos) de ese caramelo
            
            # Asignamos a la celda un diccionario con toda la información necesaria
            matriz[i][j] = {
                "tipo": tipo, # Nombre del tipo (ej: "oreo")
                "puntos": datos["puntos"], # Valor en puntos
                "img": pygame.image.load(datos["img"]), # Cargamos la imagen en memoria
                "estado": "activo" # Definimos que está activo para jugar
            }


def crear_botones_matriz_sobre_contenedor(matriz: list[list], rect_cont: pygame.Rect) -> None:
    """
    PROPOSITO:
        Calcula las dimensiones y posiciones de cada celda para que encajen proporcionalmente
        dentro del área de juego (contenedor), y les asigna un objeto pygame.Rect para manejar colisiones.

    PARAMETROS:
        * matriz: La estructura de datos del juego.
        * rect_cont: El pygame.Rect que define el área total disponible para el tablero.

    RETORNA:
        * None (Agrega la clave "rect" a cada celda de la matriz).
    """
    # Calculamos el ancho de cada celda: usamos el 98% del ancho total dividido por la cantidad de columnas
    ancho_celda_matriz = int(rect_cont.width * 0.98 / len(matriz[0]))
    
    # Calculamos el alto de cada celda: usamos el 98% del alto total dividido por la cantidad de filas
    alto_celda_matriz  = int(rect_cont.height * 0.98 / len(matriz))
    
    # Calcula un margen inicial del 1% para que la tabla quede centrada dentro del contenedor
    margen_x = int(rect_cont.width * 0.01) + rect_cont.x
    margen_y = int(rect_cont.height * 0.01) + rect_cont.y

    # Recorremos todas las filas
    for i in range(len(matriz)):
        # Recorremos todas las columnas
        for j in range(len(matriz[i])):
            
            # Creamos el objeto Rect de Pygame calculado para esta posición específica (i, j)
            un_rectangulo = pygame.Rect(
                (j * ancho_celda_matriz) + margen_x, # Posición X: columna * ancho + margen
                (i * alto_celda_matriz)  + margen_y, # Posición Y: fila * alto + margen
                ancho_celda_matriz, # Ancho calculado
                alto_celda_matriz   # Alto calculado
            )
            
            # Guardamos este rectángulo dentro del diccionario de la celda para usarlo luego (clicks/dibujo)
            matriz[i][j]["rect"] = un_rectangulo


def dibujar_matriz(matriz: list[list], pantalla: pygame.Surface, celda_sel: tuple = None) -> None:
    """
    PROPOSITO:
        Renderiza visualmente el tablero en la pantalla. Dibuja las imágenes de los caramelos
        y, si corresponde, resalta la celda seleccionada o los comodines activados.

    PARAMETROS:
        * matriz: La estructura de datos del juego.
        * pantalla: La superficie principal de Pygame donde se dibujará.
        * celda_sel: Tupla (fila, columna) con la celda seleccionada por el usuario (o None).

    RETORNA:
        * None.
    """
    filas = len(matriz)
    columnas = len(matriz[0])

    # Recorremos toda la matriz para dibujar celda por celda
    for i in range(filas):
        for j in range(columnas):
            elem = matriz[i][j] # Obtenemos el elemento actual
            
            # Verificamos si tiene una imagen cargada (si no es un espacio vacío post-eliminación)
            if elem.get("img") is not None:
                # Escalamos la imagen al tamaño actual del rectángulo (importante si cambió la resolución)
                img_escalada = pygame.transform.scale(elem["img"], (elem["rect"].width, elem["rect"].height))
                # Dibujamos la imagen escalada en la posición del rectángulo
                pantalla.blit(img_escalada, elem["rect"])
            
            # Si la celda tiene activado el efecto de comodín (combo de 5)
            if elem.get("efecto_comodin") == True:
                DORADO = (255, 215, 0) # Definimos color dorado
                # Dibujamos un recuadro grueso (5px) alrededor
                pygame.draw.rect(pantalla, DORADO, elem["rect"], 5)

            # Si la celda corresponde a la selección actual del usuario
            if celda_sel == (i, j):
                # Dibujamos un recuadro blanco (3px) para indicar selección
                pygame.draw.rect(pantalla, (255, 255, 255), elem["rect"], 3)


def intercambiar(matriz: list[list], a: tuple, b: tuple) -> None:
    """
    PROPOSITO:
        Realiza un intercambio (swap) del contenido lógico entre dos celdas dadas,
        asegurando que los rectángulos físicos (posiciones en pantalla) se mantengan en su lugar.

    PARAMETROS:
        * matriz: El tablero de juego.
        * a: Tupla (fila, columna) de la primera celda.
        * b: Tupla (fila, columna) de la segunda celda.

    RETORNA:
        * None.
    """
    r1, c1 = a # Desempaquetamos coordenadas de la celda A
    r2, c2 = b # Desempaquetamos coordenadas de la celda B
    
    # -- Intercambio Lógico (Datos) --
    aux = matriz[r1][c1].copy() # Copiamos los datos de A en auxiliar
    matriz[r1][c1] = matriz[r2][c2] # Ponemos los datos de B en A
    matriz[r2][c2] = aux # Ponemos los datos de A (aux) en B
    
    # -- Corrección Física (Rectángulos) --
    # Al mover los diccionarios, se llevaron sus posiciones rectangulares viejas.
    # Debemos intercambiar los 'rect' para que el objeto en (0,0) tenga el rect de (0,0).
    temp_rect = matriz[r1][c1]["rect"] # Guardamos rect de la nueva posición A
    
    matriz[r1][c1]["rect"] = matriz[r2][c2]["rect"] # Le asignamos a A el rect que tenía B
    matriz[r2][c2]["rect"] = temp_rect # Le asignamos a B el rect que tenía A


def son_vecinos(a: tuple, b: tuple) -> bool:
    """
    PROPOSITO:
        Determina si dos coordenadas del tablero son adyacentes de forma ortogonal
        (arriba, abajo, izquierda o derecha), ignorando diagonales.

    PARAMETROS:
        * a: Tupla (fila, columna) de origen.
        * b: Tupla (fila, columna) de destino.

    RETORNA:
        * Bool: True si son vecinos directos, False en caso contrario.
    """
    r1, c1 = a
    r2, c2 = b
    
    # Chequeamos: (Misma columna Y diferencia de 1 fila) O (Misma fila Y diferencia de 1 columna)
    es_vecino = (abs(r1 - r2) == 1 and c1 == c2) or (abs(c1 - c2) == 1 and r1 == r2)
    
    return es_vecino


def obtener_coordenada_click(matriz: list[list], pos_click: tuple) -> tuple:
    """
    PROPOSITO:
        Traduce una posición de pantalla (pixeles X, Y del mouse) a coordenadas lógicas 
        de la matriz (fila, columna).

    PARAMETROS:
        * matriz: El tablero con los rectángulos definidos.
        * pos_click: Tupla (x, y) donde se hizo click.

    RETORNA:
        * Tupla (fila, columna) si el click fue válido.
        * None si el click no cayó sobre ninguna celda.
    """
    ubicacion_click = None
    
    # Recorremos toda la matriz buscando colisión
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            
            # Usamos collidepoint del Rect para ver si el mouse tocó esta celda
            if matriz[i][j]["rect"].collidepoint(pos_click):
                ubicacion_click = (i, j) # Guardamos la coordenada encontrada
                return ubicacion_click # Retornamos inmediatamente
    
    return ubicacion_click # Retornamos None si no encontró nada


def reproducir_sonido(ruta: str) -> None:
    """
    PROPOSITO:
        Carga y reproduce un efecto de sonido dado por su ruta de archivo.
        Incluye manejo de errores para evitar caídas si falta el archivo.

    PARAMETROS:
        * ruta: Cadena con la dirección del archivo de audio.

    RETORNA:
        * None.
    """
    if ruta is not None: # Verificamos que la ruta sea válida
        try:
            sound = pygame.mixer.Sound(ruta) # Cargamos el sonido
            sound.set_volume(0.5) # Ajustamos volumen medio
            sound.play() # Reproducimos una vez
        except:
            pass # Si falla la carga, ignoramos el error silenciosamente


# -------------------------------------------------------------------------
# LÓGICA DE MATCHES Y COMBOS
# -------------------------------------------------------------------------

def hay_match_resuelto(matriz: list[list]) -> bool:
    """
    PROPOSITO:
        Escanea todo el tablero buscando si existe alguna línea de 3 o más elementos iguales.
        Se utiliza principalmente para validar que el tablero inicial no comience "roto".

    PARAMETROS:
        * matriz: El tablero a analizar.

    RETORNA:
        * Bool: True si hay al menos un match formado, False si está limpio.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # --- Verificación Horizontal ---
    for i in range(filas):
        # Iteramos hasta antepenúltima columna para poder mirar +1 y +2 sin error de índice
        for j in range(columnas - 2):
            t1 = matriz[i][j]["tipo"]
            t2 = matriz[i][j+1]["tipo"]
            t3 = matriz[i][j+2]["tipo"]
            # Si los tres tipos son iguales, hay match
            if t1 == t2 and t2 == t3:
                return True
                
    # --- Verificación Vertical ---
    for j in range(columnas):
        # Iteramos hasta antepenúltima fila para poder mirar +1 y +2 sin error de índice
        for i in range(filas - 2):
            t1 = matriz[i][j]["tipo"]
            t2 = matriz[i+1][j]["tipo"]
            t3 = matriz[i+2][j]["tipo"]
            # Si los tres tipos son iguales, hay match
            if t1 == t2 and t2 == t3:
                return True
                
    return False


def hay_jugada_posible(matriz: list[list]) -> bool:
    """
    PROPOSITO:
        Determina si el jugador tiene algún movimiento válido disponible.
        Prueba intercambiar cada celda con sus vecinos para ver si se forma un match.

    PARAMETROS:
        * matriz: El tablero actual.

    RETORNA:
        * Bool: True si existe al menos un movimiento que genere match, False si no hay movimientos.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    
    for i in range(filas):
        for j in range(columnas):
            
            # --- Prueba: Swap hacia la Derecha ---
            if j < columnas - 1: # Solo si no es la última columna
                # Hacemos el swap temporal
                matriz[i][j], matriz[i][j+1] = matriz[i][j+1], matriz[i][j]
                
                # Verificamos si formó match
                if hay_match_resuelto(matriz):
                    # Si formó match, revertimos y retornamos True (hay jugada)
                    matriz[i][j], matriz[i][j+1] = matriz[i][j+1], matriz[i][j]
                    return True
                
                # Si no formó match, revertimos el cambio para seguir buscando
                matriz[i][j], matriz[i][j+1] = matriz[i][j+1], matriz[i][j]
            
            # --- Prueba: Swap hacia Abajo ---
            if i < filas - 1: # Solo si no es la última fila
                # Hacemos el swap temporal
                matriz[i][j], matriz[i+1][j] = matriz[i+1][j], matriz[i][j]
                
                # Verificamos si formó match
                if hay_match_resuelto(matriz):
                    # Si formó match, revertimos y retornamos True
                    matriz[i][j], matriz[i+1][j] = matriz[i+1][j], matriz[i][j]
                    return True
                
                # Si no formó match, revertimos el cambio
                matriz[i][j], matriz[i+1][j] = matriz[i+1][j], matriz[i][j]
                
    return False


def matriz_es_valida(matriz: list[list]) -> bool:
    """
    PROPOSITO:
        Valida si un tablero recién generado cumple las condiciones para empezar el juego:
        1. No tiene matches ya resueltos (que exploten solos).
        2. Tiene al menos un movimiento posible para el jugador.

    PARAMETROS:
        * matriz: El tablero generado.

    RETORNA:
        * Bool: True si es válido, False si no cumple alguna condición.
    """
    # Si el tablero empieza con dulces explotando, no es válido
    if hay_match_resuelto(matriz):
        return False
    # Si el tablero no tiene movimientos posibles (está trabado), no es válido
    if not hay_jugada_posible(matriz):
        return False
    
    return True


def generar_tablero_valido_match_3(filas: int, columnas: int, elementos: dict, rect_cont: pygame.Rect) -> list[list]:
    """
    PROPOSITO:
        Genera tableros aleatorios indefinidamente hasta encontrar uno que cumpla
        todas las reglas de validez (sin matches iniciales, con jugadas posibles).

    PARAMETROS:
        * filas, columnas: Dimensiones de la matriz.
        * elementos: Diccionario de golosinas.
        * rect_cont: Rectángulo contenedor para cálculos gráficos.

    RETORNA:
        * Una matriz (lista de listas) válida y lista para jugar.
    """
    while True:
        # 1. Inicializamos matriz vacía
        matriz = inicializar_matriz(filas, columnas)
        # 2. Cargamos elementos aleatorios
        cargar_matriz_elementos(matriz, elementos)
        # 3. Calculamos los rectángulos físicos
        crear_botones_matriz_sobre_contenedor(matriz, rect_cont)
        
        # 4. Si cumple las reglas, salimos del bucle y retornamos
        if matriz_es_valida(matriz):
            return matriz


def marcar_matches(matriz: list[list], sonido_comodin, sonido_normal, coord_foco=None) -> bool:
    """
    PROPOSITO:
        Función principal de lógica de juego. Analiza el tablero para encontrar líneas de 3+.
        Detecta combos especiales (5+), gestiona la creación de comodines, reproduce sonidos
        y marca las celdas que deben ser eliminadas.

    PARAMETROS:
        * matriz: El tablero de juego.
        * sonido_comodin: Ruta o objeto de sonido para combo especial.
        * sonido_normal: Ruta o objeto de sonido para match simple.
        * coord_foco: (Opcional) Coordenada del último click para posicionar el comodín.

    RETORNA:
        * Bool: True si encontró algún match, False si no hubo coincidencias.
    """
    filas = len(matriz)
    cols = len(matriz[0])
    celdas_match = set() # Usamos un set para guardar coordenadas sin duplicados
    
    # --- 1. Búsqueda Horizontal ---
    for f in range(filas):
        contador = 1
        for c in range(1, cols):
            # Si el actual es igual al anterior
            if matriz[f][c]["tipo"] == matriz[f][c-1]["tipo"]:
                contador += 1
            else:
                # Si se corta la racha, chequeamos si llegamos a 3 o más
                if contador >= 3:
                    # Agregamos todas las celdas de esa racha al set de matches
                    for k in range(c-contador, c): celdas_match.add((f, k))
                contador = 1 # Reiniciamos contador
        
        # Chequeo final de fila (por si el match termina en el borde)
        if contador >= 3:
            for k in range(cols-contador, cols): celdas_match.add((f, k))


    # --- 2. Búsqueda Vertical ---
    for c in range(cols):
        contador = 1
        for f in range(1, filas):
            # Si el actual es igual al de arriba
            if matriz[f][c]["tipo"] == matriz[f-1][c]["tipo"]:
                contador += 1
            else:
                # Si se corta la racha, chequeamos si llegamos a 3 o más
                if contador >= 3:
                    # Agregamos todas las celdas de esa racha
                    for k in range(f-contador, f): celdas_match.add((k, c))
                contador = 1 # Reiniciamos contador
        
        # Chequeo final de columna
        if contador >= 3:
            for k in range(filas-contador, filas): celdas_match.add((k, c))


    # --- 3. Procesamiento de Resultados ---
    hay_match = False
    
    # Si encontramos alguna celda para eliminar
    if len(celdas_match) > 0:
        hay_match = True
        hubo_combo_grande = False # Bandera para saber si activar el sonido especial
        
        # Paso A: Agrupar coordenadas por color para detectar combos grandes
        grupos_por_color = {}
        for coord in celdas_match:
            f, c = coord
            color = matriz[f][c]["tipo"]
            
            if color not in grupos_por_color:
                grupos_por_color[color] = []
            grupos_por_color[color].append(coord)
            
        # Paso B: Revisar cada grupo de color
        for color in grupos_por_color:
            lista_coords = grupos_por_color[color]
            
            # Si un grupo tiene 5 o más celdas (COMBO ESPECIAL)
            if len(lista_coords) >= 5:
                hubo_combo_grande = True 
                
                # Determinamos dónde nacerá el comodín
                # Si hay un foco (click) y es parte del grupo, nace ahí. Si no, en la primera.
                if coord_foco is not None and coord_foco in lista_coords:
                    f_com, c_com = coord_foco
                else:
                    f_com, c_com = lista_coords[0]
                
                # Activamos flag visual de comodín
                matriz[f_com][c_com]["efecto_comodin"] = True
                
                # Reproducimos sonido especial
                reproducir_sonido(sonido_comodin)
                
                # Cambiamos la imagen inmediatamente para feedback visual
                try:
                    matriz[f_com][c_com]["img"] = pygame.image.load("assets/img/comodin.png")
                except:
                    pass
                
                # PODER DEL COMODÍN: Agregamos fila y columna enteras para eliminar
                for x in range(cols): celdas_match.add((f_com, x))
                for y in range(filas): celdas_match.add((y, c_com))


        # Paso C: Sonido Normal (solo si no hubo combos grandes)
        if not hubo_combo_grande:
            reproducir_sonido(sonido_normal)


        # Paso D: Marcar flag lógico 'eliminar' en todas las celdas finales
        for coord in celdas_match:
            f, c = coord
            matriz[f][c]["eliminar"] = True


    return hay_match


def eliminar_y_puntuar(matriz: list[list], elementos: dict, comodin_dict: dict) -> int:
    """
    PROPOSITO:
        Recorre la matriz ejecutando la eliminación de celdas marcadas.
        Calcula el puntaje total sumando los valores de las fichas y bonus de comodín.
        Deja las celdas eliminadas en estado 'vacio'.

    PARAMETROS:
        * matriz: El tablero de juego.
        * elementos: Diccionario de valores normales.
        * comodin_dict: Diccionario de valores del comodín.

    RETORNA:
        * int: Puntos totales acumulados en esta operación.
    """
    puntos_totales = 0
    filas = len(matriz)
    cols = len(matriz[0])
    
    # Recorremos toda la matriz
    for f in range(filas):
        for c in range(cols):
            celda = matriz[f][c]
            
            # Si la celda era un comodín naciendo (tiene el efecto activado)
            if celda.get("efecto_comodin") == True:
                puntos_totales += comodin_dict["comodin"]["puntos"] # Sumamos bonus
                celda["efecto_comodin"] = False # Apagamos efecto
                
            # Si la celda está marcada para eliminación
            if celda.get("eliminar") == True:
                puntos_totales += celda["puntos"] # Sumamos puntos del caramelo
                
                # Vaciamos la celda
                celda["estado"] = "vacio"
                celda["tipo"] = "vacio"
                celda["img"] = None
                celda["eliminar"] = False # Limpiamos flag

    return puntos_totales


def rellenar_tablero(matriz: list[list], elementos: dict) -> None:
    """
    PROPOSITO:
        Escanea el tablero buscando huecos ('estado': 'vacio') y genera nuevos
        elementos aleatorios para rellenarlos.

    PARAMETROS:
        * matriz: El tablero con huecos.
        * elementos: Diccionario de elementos disponibles para generar.

    RETORNA:
        * None (Modifica la matriz in-place).
    """
    filas = len(matriz)
    cols = len(matriz[0])
    # Lista de claves para elegir random
    lista_elem_posibles = list(elementos.keys())
    
    for f in range(filas):
        for c in range(cols):
            # Si encontramos un hueco vacío
            if matriz[f][c].get("estado") == "vacio":
                
                # Elegimos nuevo tipo
                elem_nuevo = choice(lista_elem_posibles)
                datos_elem = elementos[elem_nuevo]
                # Recuperamos el rectángulo original para mantener posición
                rect_original = matriz[f][c]["rect"]
                
                # Sobrescribimos la celda con el nuevo caramelo
                matriz[f][c] = {
                    "tipo": elem_nuevo,
                    "puntos": datos_elem["puntos"],
                    "img": pygame.image.load(datos_elem["img"]),
                    "rect": rect_original,
                    "estado": "activo"
                }


# -------------------------------------------------------------------------
# SISTEMA DE ARCHIVOS Y UTILIDADES GRÁFICAS
# -------------------------------------------------------------------------

def cargar_lista_puntajes() -> list:
    """
    PROPOSITO:
        Lee el archivo 'puntajes.csv', procesa las líneas y devuelve el Top 10.

    RETORNA:
        * Lista de tuplas (nombre, puntaje) ordenada de mayor a menor.
    """
    lista = []
    try:
        # Abrimos el archivo en modo lectura
        with open("puntajes.csv", "r") as archivo:
            for linea in archivo:
                try:
                    # Parseamos la línea csv
                    nombre, puntaje = linea.strip().split(',')
                    # Agregamos a la lista convirtiendo puntaje a int
                    lista.append((nombre, int(puntaje)))
                except ValueError:
                    continue # Saltamos líneas con errores
    except FileNotFoundError:
        return [] # Si no existe, retornamos lista vacía


    # Ordenamos la lista por puntaje (descendente)
    lista.sort(key=lambda tupla: tupla[1], reverse=True)
    
    # Retornamos solo los 10 mejores
    return lista[:10]


def escalar_fondo(ruta: str, tamanio: tuple) -> pygame.Surface:
    """
    PROPOSITO:
        Carga una imagen desde una ruta y la escala al tamaño especificado.
        
    RETORNA:
        * pygame.Surface con la imagen escalada.
    """
    return pygame.transform.scale(pygame.image.load(ruta), tamanio)


def colocar_img_boton(ruta_img: str, ancho: int, alto: int) -> pygame.Surface:
    """
    PROPOSITO:
        Carga una imagen de botón y la escala a las dimensiones deseadas.
        
    RETORNA:
        * pygame.Surface con la imagen del botón lista para usar.
    """
    img = pygame.image.load(ruta_img)
    return pygame.transform.scale(img, (int(ancho), int(alto)))
