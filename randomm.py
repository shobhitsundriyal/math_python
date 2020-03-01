import random
import turtle

t = turtle.Turtle()
wn = turtle.Screen()
turtle.bgcolor('black')
turtle.color('white')

x = 0
#t.shape('turtle')
while x < 400:
    r = random.randint(0,2)
    if r == 0:
        movement = random.randrange(20, 50)
        turtle.rt(random.randint(1,180))
        turtle.forward(movement)
    else:
        movement = random.randrange(20, 50)
        turtle.lt(random.randint(1,180))
        turtle.forward(movement)
