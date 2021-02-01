from random import *
a = []
for n in range (0,1000):
    a.append(randint(1,10000))
temp = 0
cur = 0
curInx = 0
while True:
    for inx in range (0,1000):
        check = 0
        print (a)
        cur = a[inx]
        curInx = inx
        for i in range (inx,1000):
            if a[i] < cur:
                cur = a[i]
                curInx = i         
        if curInx != inx:
            temp = a[inx]
            a[inx] = cur
            a[curInx] = temp
            check += 1
    if check == 0:
        print('Done!')
        break
