from turtle import *
import time
from random import randrange
from freegames import square, vector  
food = vector(0, 0)
snake = [vector(10, 0)] 
aim = vector(0, -10)
actual = randrange(0,4)
siguiente = randrange(0,4)
numRandX = randrange(0,2)
numRandY = randrange(0,2)
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y  
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190  
def move():
    global actual
    global siguiente
    global numRandX
    global numRandY
    "Move snake forward one segment."
    color = ''
    if actual == siguiente:
       if actual == 4:
          siguiente = 0
       else:
          siguiente = siguiente +1
    head = snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        numRandX = randrange(0,2)
        numRandY = randrange(0,2)
    else:
        snake.pop(0)

        if food.x < 150 and food.x > -150:
            if numRandX == 0:
                food.x -=1
            elif numRandX == 1:
                food.x +=1
            elif food.x > 150:
                food.x -=1
            elif food.x < -150:
                food.x +=1
            
    
    clear()
    if actual == 0:
       color = 'black'
    if actual == 1:
       color = 'blue'
    if actual == 2:
       color = 'green'
    if actual == 3:
       color = 'yellow'
    if actual == 4:
       color = 'purple'
    for body in snake:
        square(body.x, body.y, 9, color)
    if siguiente == 0:
       color = 'black'
    if siguiente == 1:
       color = 'blue'
    if siguiente == 2:
       color = 'green'
    if siguiente == 3:
       color = 'yellow'
    if siguiente == 4:
       color = 'purple'
    square(food.x, food.y, 9, color)
    update()
    ontimer(move, 100)
setup(420, 420, 370, 0)
hideturtle() 
tracer(False) 
listen() 
onkey(lambda: change(10, 0), 'Right') 
onkey(lambda: change(-10, 0), 'Left') 
onkey(lambda: change(0, 10), 'Up') 
onkey(lambda: change(0, -10), 'Down') 
move() 
done()
