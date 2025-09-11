import turtle
from turtle import *
t = Turtle()

t.shape('turtle')


def square(x, length):
    for i in range(4):
        t.forward(x)
        t.left(length)


def doubleSquares(irange):
    length = 25
    for i in range(irange):
        square(length, 90)
        length += 25
doubleSquares(5)