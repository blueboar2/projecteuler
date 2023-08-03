import math

sum = 0
nc = 1
primes = [2, 3, 5, 7, 11, 13]

def generate():
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

def divisors(sum):
    nump = []
    for i in primes:

        if sum == 1:
            break

        j = 0
        while sum % i == 0:
            sum = sum // i
            j += 1

        if j > 0:
            nump.append(j + 1)

    num = 1
    for i in nump:
        num *= i

    return num

while True:
    generate()
    sum = sum + nc
    divi = divisors(sum)

    if divi > 500:
        print(nc)
        print(sum)
        break

    nc += 1
