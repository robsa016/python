import turtle

def koch_curve(t, ite, length, shortening_factor, angle):
    
    if ite == 0:
        t.forward(length)
        return
    
    ite = ite - 1
    length = length / shortening_factor
    
    koch_curve(t, ite, length, shortening_factor, angle)

    t.left(angle)
    koch_curve(t, ite, length, shortening_factor, angle)

    t.right(angle * 2)
    koch_curve(t, ite, length, shortening_factor, angle)

    t.left(angle)
    koch_curve(t, ite, length, shortening_factor, angle)


t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("black", "light blue")

t.penup()
t.setpos(-325,180)
t.pendown()

t.begin_fill()

for i in range(3):
  koch_curve(t, 5, 650, 3, 60)
  t.right(120)

t.end_fill()
  
turtle.mainloop()
