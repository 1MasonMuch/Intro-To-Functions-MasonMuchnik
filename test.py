import turtle
from turtle import *
t = Turtle()

t.shape('turtle')



t.speed(10)

def square():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(-5)






def doubleSquare(irange):
    length = 5
    for i in range(irange):
        square(length, 90)
        length += 1
doubleSquare(60) 