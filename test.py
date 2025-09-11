import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

def square():
    for i in range(4):
        t.forward(100)
        t.left(90)



for i in range(60):
    square()
    t.right(5)