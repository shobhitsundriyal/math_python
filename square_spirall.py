from turtle import *
from random import randint 

speed(0)
bgcolor('black')
x = 1

while x < 400:

    r = randint(0,255) #makes variables r,g,b whose value is an integer,
    g = randint(0,255) # which is between 0 and 255. It is random, and
    b = randint(0,255) # changes every time the loop runs

    colormode(255)
    pencolor(r,g,b) 

    fd(50 + x)
    rt(90.911)
    x = x+1 

exitonclick() 