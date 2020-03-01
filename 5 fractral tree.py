import turtle


turtle.bgcolor('black')
#turtle.color('white')

t = turtle.Turtle()
t.color('brown')
t.left(90)
t.speed(250)

def tree(len):
    if len < 35:
        t.color('green')
    else:
        t.color('brown')
    if len < 10:
        return
    else:
        t.forward(len)
        t.left(30)
        tree(3 * len/4)
        t.right(60)
        tree(3 * len/4)
        t.left(30)
        if len > 35:
            t.color('brown')
        t.backward(len)

tree(100)

turtle.done()