from turtle import *
a = Turtle()
a.hideturtle()
a.speed(0)
a.color("black")
a.width(2)


r=255
g=0
b=0

mode = 0

num1 = 10
num2 = 2

n = 1530/num1

a.left(180/num2)

for i in range (num1):


    rx = "000" + str(hex(round(r)))
    rx = rx[len(rx)-2:len(rx)]
    if rx[0] == 'x':
        rx = "0" + rx[len(rx)-1:len(rx)]

    gx = "000" + str(hex(round(g)))
    gx = gx[len(gx)-2:len(gx)]
    if gx[0] == 'x':
        gx = "0" + gx[len(gx)-1:len(gx)]

    bx = "000" + str(hex(round(b)))
    bx = bx[len(bx)-2:len(bx)]
    if bx[0] == 'x':
        bx = "0" + bx[len(bx)-1:len(bx)]

    a.color(("#"+rx+gx+bx))

    
    for i in range(num2):
        a.fd(720/num2)
        a.lt(360/num2)
    a.lt(360/num1)


    if mode == 0:
        g+=n
        if g >= 255-n:
            g = 255
            mode +=1
    elif mode == 1:
        r-=n
        if r <= n-1:
            r = 0
            mode +=1
    elif mode == 2:
        b+=n
        if b >= 255-n:
            b = 255
            mode +=1
    elif mode == 3:
        g-=n
        if g <= n-1:
            g = 0
            mode +=1
    elif mode == 4:
        r+=n
        if r >= 255-n:
            r = 255
            mode +=1
    elif mode == 5:
        b-=n
        if b <= n-1:
            b = 0
            mode = 0
