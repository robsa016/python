primes = []
isPrime = True
for i in range (2,1000000):
    isPrime = True
    for p in primes:
        if i % p == 0:
            isPrime = False
            break
    if (isPrime):
        primes.append(i)
        print(i)
