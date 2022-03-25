"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
taps = 0
cont =0


def square(x, y):
    """Dibuja cuadrados con marco negro."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convierte las cordenada x,y en index de los cuadrados."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convierte los cuadrados en coordenadas x y y."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    global cont
    global taps
    taps+=1
    print('Taps',taps)
    # usamos el contador global para contar los taps
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        cont = cont +1
        if cont == 32:
            print('Completado')
        #En caso de terminar de encontrar los pares imprimir completado


def draw():
    """Dibuja la imagen."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        style =('Arial', 30, 'normal') 
        #centramos los numeros.
        if tiles[mark] < 10:
            goto(x+20, y)
            color('black')
            write(tiles[mark], font=style)
        elif tiles[mark] >= 10:
            goto(x+10, y)
            color('black')
            write(tiles[mark], font=style)
            

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
