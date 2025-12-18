🍬 Candy-Combo

Candy-Combo es un juego tipo match 3 inspirado en Candy Crush, desarrollado en Python con Pygame.
El objetivo es intercambiar golosinas en un tablero para formar combinaciones, generar comodines y obtener la mayor puntuación posible.

🎮 Características principales

Tablero de 8x8 con golosinas aleatorias.

Detección de matches horizontales y verticales.

Combinaciones de 5 o más generan comodines que eliminan filas y columnas.

Sistema de puntajes Top 10 usando archivos CSV.

Fondos y botones escalables según la resolución de pantalla.

Efectos de sonido para combos, comodines y clicks.

Compatible con resoluciones: 1920x1000, 1600x1000, 1440x900.

🛠️ Tecnologías utilizadas

Python 3.x

Pygame

Archivos CSV para guardar puntajes

📂 Estructura del proyecto
Candy-Combo/
├── assets/
│   ├── img/                 # Imágenes de fondos, botones y caramelos
│   │   ├── fondo_juego.png
│   │   ├── logo.png
│   │   └── ...
│   ├── audio/               # Sonidos y música
│   │   ├── victoria.wav
│   │   └── ...
├── main.py                  # Archivo principal del juego
├── funciones.py             # Funciones de lógica, tablero y gráficos
├── constantes.py            # Colores, rutas de imágenes y sonidos, resoluciones
├── puntajes.csv             # Archivo para guardar Top 10
└── README.md

⚙️ Requisitos e instalación

Instalar Python 3.x: https://www.python.org/downloads/

Instalar Pygame:

pip install pygame


Clonar o descargar este repositorio.

Ejecutar el juego:

python main.py

🕹️ Cómo jugar

Intercambia caramelos adyacentes para formar combinaciones de 3 o más.

Formar una combinación de 5 o más genera un comodín especial.

Los comodines eliminan fila y columna completa, aumentando tu puntuación.

Acumula puntos y trata de llegar al Top 10.

Usa los botones del menú para:

Botón	Función
Jugar	Inicia una partida
Puntajes	Muestra el Top 10
Resolución	Cambia la resolución de pantalla
Salir	Cierra el juego
🔑 Funciones clave del código
Función	Propósito
generar_tablero_valido_match_3()	Crea un tablero inicial válido sin matches y con jugadas posibles.
marcar_matches()	Detecta matches y combos especiales, reproduce sonidos y marca celdas para eliminar.
eliminar_y_puntuar()	Elimina celdas marcadas y suma puntos.
rellenar_tablero()	Rellena huecos con nuevos elementos aleatorios.
dibujar_matriz()	Dibuja el tablero y efectos visuales en pantalla.
cargar_lista_puntajes()	Carga y ordena el Top 10 desde puntajes.csv.
🎨 Assets

Golosinas: imágenes .png de caramelos.

Fondos: pantallas de juego, menú, puntajes y registro.

Sonidos: efectos de clic, combos, comodines y música de fondo.

📜 Licencia

Proyecto educativo, desarrollado con fines de aprendizaje.
Puede modificarse y distribuirse libremente.
