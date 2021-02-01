from sys import *
checks = {3:"Fizz",5:"Buzz"}
for i in range(1, 101):
    multiples = []
    for j in checks.keys():
        if i % j == 0:
            multiples.append(checks[j])
    if len(multiples) == 0:
        print (i)
    else:
        for k in multiples:
            stdout.write(k)
        print()
