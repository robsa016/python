from turtle import *
t = Turtle()
t.speed(1000)
t.color("black","light blue")
t.width(1)

t.begin_fill()


for i in range (0,1000):
    t.forward(i/20)
    t.left(10)

t.end_fill()
