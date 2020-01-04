from turtle import *

def square(l):
    for i in range(4):
        forward(l)
        right(90)

k = 5
for i in range(80):
    square(k)
    right(5)
    k += 5