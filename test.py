import turtle
from turtle import *
t = Turtle()

t.shape('turtle')



t.speed(10)

for i in range(4):
    def square(x,y):
        t.forward(x)
        t.left(y)





def doubleSquare(irange):
    length = 5
    for i in range(irange):
        square(length, 90)
        length = length + 5
doubleSquare(60) 