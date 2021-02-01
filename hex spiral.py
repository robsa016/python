from turtle import *
t = Turtle()
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "magenta"]
bgcolor("black")
t.hideturtle()
t.width(1)

for i in range (0,10000):
    t.color(colors[i%6])
    t.forward(i/2)
    t.left(59)
