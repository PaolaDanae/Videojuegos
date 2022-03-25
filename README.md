# Documentation Videogames Project
Modify freegames source code

1. PAINT VIDEOGAME DOCUMENTATION
-def line(start, end):
    """Ubica un punto inicial y uno final para hacer una linea entre ambos puntos."""
-def square(start, end):
    """Crea un cuadrado con la distancia del punto inicial al final."""
-def circle(start, end):
    """dibuja un circulo con un radio que vale la distancia entre el punto inicial y el final."""
-def rectangle(start, end):
    """Dibujar un rectangulo de esquina a esquina. deben ser esquinas opuestas"""
-def triangle(start, end):
    """Dibujar un triangulo con la primera esquina y la parte superior del triangulo."""
-def tap(x, y):
    """Obtiene la posicion inicial o la figura."""


2.SNAKE VIDEOGAME DOCUMENTATION
-def change(x, y):
    "Cambia la direccion de la vibora asignando nuevos valores en x y y al vector de posicion"
-def inside(head):
    "Regresa verdadero si la cabeza de la vibora se encuentra aun en los limites del mapa"
-def move():
    "Mueve la serpiente adelante un segmento a la vez revisando que la serpiente se encuentre dentro de los limites del mapa"
    "Cuando la serpiente alcance la comida, la comida comenzara a moverse hacia la izq o der de forma aleatoria"
    "Se genera un color aleatorio para la vibora y la fruta utilizando una serie de ifs"
    
3.PAC-MAN VIDEOGAME DOCUMENTATION
-Al principio hay un gran vector que es la creación del mapa
-def square(x, y):
    "dibuja cuadrados usando el camino."
-def offset(point):
    "regresa de que tipo son los cuadrados."
-def valid(point):
    "Regresa verdadero si la posicion del punto es valido."
-def world():
    "Usando el path crea el punto ."
-def move():
    "Mueve a pac_man y a los fantasmas, con velocidad e inteligencia."
    "Se mejora la inteligencia de los fantasmas con ifs"
-def change(x, y):
    "Cambia la direccion si se puede."
    
4.PARABOLA VIDEOGAME DOCUMENTATION
-def tap(x, y):
    "Responde a el tap del mouse."
-def inside(xy):
    "Regresa verdadero si esta dentro los circulos."
-def draw():
    "Dibuja la bola y los objetivos circulares."
-def move():
    "Mover la pelota y los objetivos."
    
5.MEMORY VIDEOGAME DOCUMENTATION
-def square(x, y):
    """Dibuja cuadrados con marco negro."""
-def index(x, y):
    """Convierte las cordenada x,y en index de los cuadrados."""
-def xy(count):
    """Convierte los cuadrados en coordenadas x y y."""
-def tap(x, y):
    """Update mark and hidden tiles based on tap."""
-def draw():
    """Dibuja la imagen."""
