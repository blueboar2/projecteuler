import math

primes = [2, 3, 5, 7, 11, 13]
num = 6
cur = 14

while num != 10001:
    dok = int(math.sqrt(cur)) + 1
    for i in primes:
        if i > dok:
            primes.append(cur)
            num += 1
            break
        if cur % i == 0:
            break

    cur += 1

print(primes[-1])