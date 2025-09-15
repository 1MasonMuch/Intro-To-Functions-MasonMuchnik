import turtle
from turtle import *
t = Turtle()

t.shape('turtle')



t.speed(120)



def square(x,y):
    for i in range(4):

        t.forward(x)
        t.left(y)






def doubleSquare(irange):
    length = 5
    for i in range(irange):
        square(length, 90)
        length = length + 5
        t.right(5)
doubleSquare(60) 