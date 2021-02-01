from turtle import *
t = Turtle()
colors = ["red", "blue", "yellow", "green", "blue", "magenta"]
t.speed(0)
t.hideturtle()
t.color("blue")
t.width(1)

dist = 200

t.penup()
t.setx(-dist)
t.pendown()
t.color(colors[1])
for i in range (0,180):
    t.fd(dist)
    t.color(colors[i%2])
    t.fd(dist)
    t.rt(177)
