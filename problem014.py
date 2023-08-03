max = 0
ch = 0

def collatz(num):
    kol = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        kol += 1
    return kol

for i in range(1, 1000000 + 1):
    dl = collatz(i)
    if dl > max:
        max = dl
        ch = i

print(ch)