import math

primes = [2, 3, 5, 7, 11, 13]
cur = 14

while primes[-1] < 2000000:
    dok = int(math.sqrt(cur)) + 1
    for i in primes:
        if i > dok:
            primes.append(cur)
            break
        if cur % i == 0:
            break

    cur += 1

print(sum(primes) - primes[-1])