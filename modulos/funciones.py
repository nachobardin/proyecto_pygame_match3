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
    PROPOSITO: Recorre la matriz y rellena cada celda con un elemnto aleatorio del diccionario de elementos.

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
    PROPOSITO: Determina las dimensiones y posiciones de las celdas del tablero dentro del contenedor dado.

    PARAMETROS:
        * matriz: La matriz del juego.
        * rect_cont: El rect contenedor que define el área total disponible para el tablero.

    RETORNA: None.
    """
    # Calculamos el ancho de cada celda
    ancho_celda_matriz = int(rect_cont.width * 0.98 / len(matriz[0]))
    
    # Calculamos el alto de cada celda
    alto_celda_matriz  = int(rect_cont.height * 0.98 / len(matriz))
    
    # Calcula un margen inicial
    margen_x = int(rect_cont.width * 0.01) + rect_cont.x
    margen_y = int(rect_cont.height * 0.01) + rect_cont.y

    # Recorremos todas las filas
    for i in range(len(matriz)):
        # Recorremos todas las columnas
        for j in range(len(matriz[i])):
            
            # Crea el objeto Rect calculado para la posición(i, j)
            un_rectangulo = pygame.Rect(
                (j * ancho_celda_matriz) + margen_x, # Posición X: columna * ancho + margen
                (i * alto_celda_matriz)  + margen_y, # Posición Y: fila * alto + margen
                ancho_celda_matriz, # Ancho calculado
                alto_celda_matriz   # Alto calculado
            )
            
            # Guarda el rectangulo dentro del diccionario de la celda para usarlo despues (clicks/dibujo)
            matriz[i][j]["rect"] = un_rectangulo


def dibujar_matriz(matriz: list[list], pantalla: pygame.Surface, celda_sel: tuple = None) -> None:
    """
    PROPOSITO: Renderizar el tablero en la pantalla. Dibuja las imágenes de los elementos

    PARAMETROS:
        * matriz: La matriz del jeugo.
        * pantalla: La superficie donde se va a dibujar.
        * celda_sel: Ubicacion con la celda seleccionada por el usuario (o None).

    RETORNA: None.
    """
    filas = len(matriz)
    columnas = len(matriz[0])

    # Recorremos toda la matriz para dibujar celda por celda
    for i in range(filas):
        for j in range(columnas):
            elem = matriz[i][j] # El elemento actual
            
            # Verifica si tiene una imagen cargada 
            if elem.get("img") is not None:
                # Escala la imagen al tamanio actual del rectángulo 
                img_escalada = pygame.transform.scale(elem["img"], (elem["rect"].width, elem["rect"].height))
                # Dibuja la imagen escalada en la posición del rectángulo
                pantalla.blit(img_escalada, elem["rect"])
            
            # Si la celda tiene activado el efecto de comodín 
            if elem.get("efecto_comodin") == True:
                DORADO = (255, 215, 0) 
                # Dibuja el recuadro dorado
                pygame.draw.rect(pantalla, DORADO, elem["rect"], 5)

            # Si la celda corresponde a la seleccionada por el usuario
            if celda_sel == (i, j):
                # Dibuja un recuadro blanco para indicar selección
                pygame.draw.rect(pantalla, (255, 255, 255), elem["rect"], 3)


def intercambiar(matriz: list[list], a: tuple, b: tuple) -> None:
    """
    PROPOSITO: Realiza un intercambio (swappeo) del contenido entre dos celdas dadas.

    PARAMETROS:
        * matriz: El tablero de juego.
        * a: Tupla (fila, columna) de la primera celda.
        * b: Tupla (fila, columna) de la segunda celda.

    RETORNA: None.
    """
    f1, c1 = a # Desempaqueta coordenadas de la celda A
    f2, c2 = b # Desempaqueta coordenadas de la celda B
    
    #  Intercambio (Datos) 
    aux = matriz[f1][c1].copy() # Copiamos los datos de A en auxiliar
    matriz[f1][c1] = matriz[f2][c2] # Ponemos los datos de B en A
    matriz[f2][c2] = aux # Ponemos los datos de A (aux) en B
    
    #  Intercambio (Rectángulos) 
    temp_rect = matriz[f1][c1]["rect"] # Guardamos rect de la nueva posición A
    
    matriz[f1][c1]["rect"] = matriz[f2][c2]["rect"] # Le asignamos a A el rect que tenía B
    matriz[f2][c2]["rect"] = temp_rect # Le asignamos a B el rect que tenía A


def son_vecinos(a: tuple, b: tuple) -> bool:
    """
    PROPOSITO: Determina si dos coordenas del tablero son vecinas directas.

    PARAMETROS:
        * a: Tupla (fila, columna) de origen.
        * b: Tupla (fila, columna) de destino.

    RETORNA: Bool: True si son vecinos, False en caso contrario.
    """
    f1, c1 = a
    f2, c2 = b
    
    # Misma columna, la fila cambia en 1 (Arriba o Abajo)
    if c1 == c2 and (f1 - f2 == 1 or f1 - f2 == -1):
        es_vecino = True
        
    # Misma fila, la columna cambia en 1 (Izquierda o Derecha)
    elif f1 == f2 and (c1 - c2 == 1 or c1 - c2 == -1):
        es_vecino = True
        
    # No son adyacentes
    else:
        es_vecino = False
        
    return es_vecino



def obtener_coordenada_click(matriz: list[list], pos_click: tuple) -> tuple:
    """
    PROPOSITO: Retorna la coordenada lógica (fila, columna) correspondiente al lugar donde se hizo click.

    PARAMETROS:
        * matriz: El tablero con los rectángulos definidos.
        * pos_click: Tupla (x, y) donde se hizo click.

    RETORNA:
        * Tupla (fila, columna) si encontro click en celda.
        * None si el click no fue sobre ninguna celda.
    """
    ubicacion_click = None
    
    # Recorremos la matriz buscando colisión
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            
            # Usamos collidepoint del Rect para ver si el mouse toco esta celda
            if matriz[i][j]["rect"].collidepoint(pos_click):
                ubicacion_click = (i, j) # Guardamos la coordenada 
                return ubicacion_click # Retornamos ubicacion
    
    return ubicacion_click # Retornamos None si no encontró nada


def reproducir_sonido(ruta: str) -> None:
    """
    PROPOSITO: Cargar y reproducir un efecto de sonido.
        
    PARAMETROS:
        * ruta: Dirección del archivo de audio.

    RETORNA: None.
    """
    if ruta != None: # Verificamos que la ruta sea valida
        try:
            sound = pygame.mixer.Sound(ruta) # Cargamos el sonido
            sound.set_volume(0.5) # Ajustamos volumen medio
            sound.play() # Reproducimos una vez
        except:
            pass # Si falla la carga ignoramos el error



# LÓGICA DE MATCHES Y COMBOS


def hay_match_resuelto(matriz: list[list]) -> bool:
    """
    PROPOSITO: Determina si existe al menos un match resuelto en el tablero.

    PARAMETROS:
        * matriz: El tablero a analizar.

    RETORNA: Bool: True si hay al menos un match formado, False caso contrario.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    
    #  Verificación Horizontal
    for i in range(filas):
        # Itera hasta la antepenultima columna para poder mirar +1 y +2 sin error de indice
        for j in range(columnas - 2):
            t1 = matriz[i][j]["tipo"]
            t2 = matriz[i][j+1]["tipo"]
            t3 = matriz[i][j+2]["tipo"]
            # Si los tres tipos son iguales, hay match
            if t1 == t2 and t2 == t3:
                return True
                
    #  Verificación Vertical
    for j in range(columnas):
        # Itera hasta antepenultima fila para poder mirar +1 y +2 sin error de indice
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
    PROPOSITO: Determina si el jugador tiene algún movimiento válido disponible.

    PARAMETROS:
        * matriz: El tablero actual.

    RETORNA: Bool: True si existe al menos un movimiento que genere match, False caso contrario.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    
    for i in range(filas):
        for j in range(columnas):
            
            #  Swap hacia la derecha
            if j < columnas - 1: # Solo si no es la ultima columna
                # Hace el swap temporal
                matriz[i][j], matriz[i][j+1] = matriz[i][j+1], matriz[i][j]
                
                # Verifica si formo match
                if hay_match_resuelto(matriz):
                    # Si formo match, revierte y retorna True
                    matriz[i][j], matriz[i][j+1] = matriz[i][j+1], matriz[i][j]
                    return True
                
                # Si no formo match, revierte el cambio para seguir buscando
                matriz[i][j], matriz[i][j+1] = matriz[i][j+1], matriz[i][j]
            
            #  Swap hacia Abajo
            if i < filas - 1: # Solo si no es la última fila
                # Hace el swap temporal
                matriz[i][j], matriz[i+1][j] = matriz[i+1][j], matriz[i][j]
                
                # Verifica si formo match
                if hay_match_resuelto(matriz):
                    # Si formo match, revierte y retorna True
                    matriz[i][j], matriz[i+1][j] = matriz[i+1][j], matriz[i][j]
                    return True
                
                # Si no formo match, revierte el cambio
                matriz[i][j], matriz[i+1][j] = matriz[i+1][j], matriz[i][j]
                
    return False


def matriz_es_valida(matriz: list[list]) -> bool:
    """
    PROPOSITO: Valida si un tablero recién generado cumple las condiciones para empezar el juego:

    PARAMETROS:
        * matriz: El tablero generado.
    
    OBSERVACIONES:
        * Un tablero es valido si: no tiene matches resueltos y tiene jugadas posibles.
    
    RETORNA: Bool: True si es válido, False caso contrario.
    """
    # Si el tablero empieza con match, no es valido
    if hay_match_resuelto(matriz):
        return False
    # Si el tablero no tiene movimientos posibles, no es valido
    if not hay_jugada_posible(matriz):
        return False
    
    return True


def generar_tablero_valido_match_3(filas: int, columnas: int, elementos: dict, rect_cont: pygame.Rect) -> list[list]:
    """
    PROPOSITO: Genera tableros aleatorios indefinidamente hasta encontrar uno que cumpla.

    PARAMETROS:
        * filas, columnas: Dimensiones de la matriz.
        * elementos: Diccionario de golosinas.
        * rect_cont: Rectángulo contenedor para cálculos gráficos.

    RETORNA:Una matriz válida para jugar.
    """
    while True:
        # Inicializa la matriz vacía
        matriz = inicializar_matriz(filas, columnas)
        # Carga elementos aleatorios
        cargar_matriz_elementos(matriz, elementos)
        # Calcula los rectangulos
        crear_botones_matriz_sobre_contenedor(matriz, rect_cont)
        
        # Si cumple con todo sale del bucle y retorna
        if matriz_es_valida(matriz):
            return matriz


def marcar_matches(matriz: list[list], sonido_comodin, sonido_normal, coord_click=None) -> bool:
    """
    PROPOSITO: Analizar el tablero para encontrar y marcar matches de 3 o mas, gestionar combos especiales, reproducir sonidos y marcar las celdas para eliminar.

    PARAMETROS:
        * matriz: El tablero de juego.
        * sonido_comodin: Ruta o objeto de sonido para combo especial.
        * sonido_normal: Ruta o objeto de sonido para match simple.
        * coord_click: Coordenada del último click para posicionar el comodín.

    RETORNA: Bool: True si encontro algun match, False caso contrario.
    """
    filas = len(matriz)
    cols = len(matriz[0])
    celdas_match = set() # Usamos un set para guardar coordenadas sin duplicados
    
    # Búsqueda Horizontal
    for f in range(filas):
        contador = 1
        for c in range(1, cols):
            # Si el actual es igual al anterior
            if matriz[f][c]["tipo"] == matriz[f][c-1]["tipo"]:
                contador += 1
            else:
                # Si se corta la racha, chequea si llega a 3 o más
                if contador >= 3:
                    # Agrega todas las celdas de la racha al set de matches
                    for k in range(c-contador, c): celdas_match.add((f, k))
                contador = 1 # Reiniciamos contador
        
        # Chequeo final de fila (por si el match termina en el borde)
        if contador >= 3:
            for k in range(cols-contador, cols): celdas_match.add((f, k))


    #  Búsqueda Vertical 
    for c in range(cols):
        contador = 1
        for f in range(1, filas):
            # Si el actual es igual al de arriba
            if matriz[f][c]["tipo"] == matriz[f-1][c]["tipo"]:
                contador += 1
            else:
                # Si se corta la racha, chequea si llega a 3 o más
                if contador >= 3:
                    # Agrega todas las celdas de esa racha
                    for k in range(f-contador, f): celdas_match.add((k, c))
                contador = 1 # Reinicia contador
        
        # Chequeo final de columna
        if contador >= 3:
            for k in range(filas-contador, filas): celdas_match.add((k, c))


    # Procesamiento de Resultados
    hay_match = False
    
    # Si encuentra alguna celda para eliminar
    if len(celdas_match) > 0:
        hay_match = True
        hubo_combo_grande = False # Bandera para saber si se activa el sonido especial
        
        # Agrupa ubicaciones por color para detectar combos grandes
        grupos_por_tipo = {}
        for ubi in celdas_match:
            f, c = ubi
            color = matriz[f][c]["tipo"]
            
            if color not in grupos_por_tipo:
                grupos_por_tipo[color] = []
            grupos_por_tipo[color].append(ubi)
            
        # Revisa cada grupo de color
        for color in grupos_por_tipo:
            lista_coords = grupos_por_tipo[color]
            
            # Si un grupo tiene 5 o más celdas (COMBO ESPECIAL)
            if len(lista_coords) >= 5:
                hubo_combo_grande = True 
                
                # Determina donde nace el comodín
                # Si hay un click y es parte del grupo, nace ahi
                if coord_click is not None and coord_click in lista_coords:
                    f_com, c_com = coord_click
                else:
                    f_com, c_com = lista_coords[0]
                
                # Activa bandera de comodin
                matriz[f_com][c_com]["efecto_comodin"] = True
                
                # Reproduce sonido especial
                reproducir_sonido(sonido_comodin)
                
                # Cambia la imagen inmediatamente
                try:
                    matriz[f_com][c_com]["img"] = pygame.image.load("assets/img/comodin.png")
                except:
                    pass
                
                # Por el poder del comodin, Agrega fila y columna enteras para eliminar
                for x in range(cols): celdas_match.add((f_com, x))
                for y in range(filas): celdas_match.add((y, c_com))


        # Sonido normal (solo si no hubo combos grandes)
        if not hubo_combo_grande:
            reproducir_sonido(sonido_normal)


        # Marcar bandera 'eliminar' en todas las celdas finales
        for ubi in celdas_match:
            f, c = ubi
            matriz[f][c]["eliminar"] = True


    return hay_match


def eliminar_y_puntuar(matriz: list[list], elementos: dict, comodin_dict: dict) -> int:
    """
    PROPOSITO: Recorre la matriz ejecutando la eliminación de celdas marcadas y calcula el puntaje total.

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
                puntos_totales += celda["puntos"] # Sumamos puntos del elemento
                
                # Vaciamos la celda
                celda["estado"] = "vacio"
                celda["tipo"] = "vacio"
                celda["img"] = None
                celda["eliminar"] = False # Limpiamos bandera

    return puntos_totales


def rellenar_tablero(matriz: list[list], elementos: dict) -> None:
    """
    PROPOSITO: Determina si el tablero tiene huecos y los rellena con nuevos elementos aleatorios.

    PARAMETROS:
        * matriz: El tablero con huecos.
        * elementos: Diccionario de elementos disponibles para generar.

    RETORNA: None.
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
                
                # Sobrescribimos la celda con el nuevo elemento
                matriz[f][c] = {
                    "tipo": elem_nuevo,
                    "puntos": datos_elem["puntos"],
                    "img": pygame.image.load(datos_elem["img"]),
                    "rect": rect_original,
                    "estado": "activo"
                }



# SISTEMA DE ARCHIVOS Y VISUALES


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



mi_diccionario = {
    "nombre": "Ignacio",
    "apellido": "Bardin"
}

def escalar_fondo(ruta: str, tamanio: tuple) -> pygame.Surface:
    """
    PROPOSITO: Carga una imagen desde una ruta y la escala al tamaño especificado.
    
    PARAMETROS:
        * ruta: Ruta del archivo de imagen.
        * tamanio: Tupla con el tamaño deseado (ancho, alto).

    RETORNA:
        * pygame.Surface con la imagen escalada.
    """
    return pygame.transform.scale(pygame.image.load(ruta), tamanio)


def colocar_img_boton(ruta_img: str, ancho: int, alto: int) -> pygame.Surface:
    """
    PROPOSITO: Cargar y escalar imagen de botón.
    
    PARAMETROS:
        * ruta_img: Ruta del archivo de imagen.
        * ancho: Ancho deseado del botón.
        * alto: Alto deseado del botón.
    
    RETORNA:
        * pygame.Surface con la imagen del botón lista para usar.
    """
    img = pygame.image.load(ruta_img)
    return pygame.transform.scale(img, (int(ancho), int(alto)))