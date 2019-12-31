from turtle import *

def square(l):
    for i in range(4):
        forward(l)
        right(90)

for i in range(60):
    square(100)
    right(5)