from turtle import *
t = Turtle()
t.speed(1000)

bgcolor("black")
t.hideturtle()
t.width(1)

r=255
g=0
b=0

mode = 0

for i in range (0,10000):

    rx = "000" + str(hex(r))
    rx = rx[len(rx)-2:len(rx)]
    if rx[0] == 'x':
        rx = "0" + rx[len(rx)-1:len(rx)]

    gx = "000" + str(hex(g))
    gx = gx[len(gx)-2:len(gx)]
    if gx[0] == 'x':
        gx = "0" + gx[len(gx)-1:len(gx)]

    bx = "000" + str(hex(b))
    bx = bx[len(bx)-2:len(bx)]
    if bx[0] == 'x':
        bx = "0" + bx[len(bx)-1:len(bx)]
    
    t.color(("#"+rx+gx+bx))
    t.forward(i/2)
    t.left(59)

    if mode == 0:
        g+=1
        if g == 255:
            mode +=1
    elif mode == 1:
        r-=1
        if r == 0:
            mode +=1
    elif mode == 2:
        b+=1
        if b == 255:
            mode +=1
    elif mode == 3:
        g-=1
        if g == 0:
            mode +=1
    elif mode == 4:
        r+=1
        if r == 255:
            mode +=1
    elif mode == 5:
        b-=1
        if b == 0:
            mode = 0
