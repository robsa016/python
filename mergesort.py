from random import *
import time


def merge(a, b):
    c = []

    while len(a) > 0 and len(b) > 0:
        if a[0] >= b[0]:
            c.append(b[0])
            del b[0]
        elif b[0] >= a[0]:
            c.append(a[0])
            del a[0]

    while len(a) > 0:
        c.append(a[0])
        del a[0]

    while len(b) > 0:
        c.append(b[0])
        del b[0]

    return c


def mergesort(a: list):
    n = len(a)
    if n <= 1:
        return a

    array_one: list = a[0:int(n / 2)]
    array_two: list = a[int(n / 2):n]

    array_one = mergesort(array_one)
    array_two = mergesort(array_two)

    return merge(array_one, array_two)


k = 10000
array = []
for i in range(k):
    array.append(randint(1, k))
t = time.perf_counter()
print(mergesort(array))
t = time.perf_counter() - t
print("(" + str(round(t, 3)) + " sec)")
