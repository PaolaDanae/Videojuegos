"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
import math

from freegames import vector


def line(start, end):
    """Ubica un punto inicial y uno final para hacer una linea entre ambos puntos."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Crea un cuadrado con la distancia del punto inicial al final."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """dibuja un circulo con un radio que vale la distancia entre el punto inicial y el final."""
    up()
    goto(start.x,start.y)
    down()
    dist=2*math.pi*(start.x - end.x)/360
    begin_fill()
    for count in range(360):
        forward(dist)
        right(1.0)
    end_fill()
    

def rectangle(start, end):
    """Dibujar un rectangulo de esquina a esquina. deben ser esquinas opuestas"""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    forward(end.x - start.x)
    left(90)
    forward(end.y - start.y)
    left(90)
    forward(end.x - start.x)
    left(90)
    forward(end.y - start.y)
    end_fill()

def triangle(start, end):
    """Dibujar un triangulo con la primera esquina y la parte superior del triangulo."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    forward(2*(end.x - start.x))
    goto(end.x, end.y)
    goto(start.x, start.y)
    end_fill()
  
def tap(x, y):
    """Obtiene la posicion inicial o la figura."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('coral'), 'C')
onkey(lambda: color('turquoise'),'T')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
