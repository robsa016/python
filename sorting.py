from random import *
a = []
for n in range (0,100):
    a.append(randint(1,1000))
for inx in range (0,100):
    print (a)
    cur = a[inx]
    curInx = inx
    for i in range (inx,100):
        if a[i] < cur:
            cur = a[i]
            curInx = i
    if curInx != inx:
        temp = a[inx]
        a[inx] = cur
        a[curInx] = temp
print('Done!')
