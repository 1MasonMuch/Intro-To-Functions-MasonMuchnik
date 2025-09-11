import turtle
from turtle import *
t = Turtle()

t.shape('turtle')


def square():
    for i in range(4):
        t.forward(100)
        t.left(90)



def doublesquares(irange):
    length = 25
    square(length, 90)
    length = length * 2
doublesquares(5)
