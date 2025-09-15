import turtle
from turtle import *
t = Turtle()

t.shape('turtle')



t.speed(150)

def star(x,y):
    for i in range(5):

        t.forward(x)
        t.left(y)






def doubleStar(irange):
    length = 5
    for i in range(irange):
        star(length, 144)
        length = length + 5
        t.right(5)
doubleStar(65) 