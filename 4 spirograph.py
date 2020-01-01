import turtle

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0.5)

col = ['red', 'magenta', 'blue', 'cyan', 'green', 'yellow', 'white']

for i in range(60):
    for color in col:
        turtle.color(color)
        turtle.circle(100)
        turtle.left(10)