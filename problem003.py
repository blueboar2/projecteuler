import math

num = 600851475143
primefactors = []

while num != 1:
    nf = int(math.sqrt(num)) + 1
    for i in range(2, nf):
        if num % i == 0:
            primefactors.append(i)
            num //= i

print(max(primefactors))
