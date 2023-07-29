sum = 2
terms = [1, 2, 3, 5]

while terms[-1] <= 4000000:
    if terms[-1] % 2 == 0:
        sum += terms[-1]
    terms.append(terms[-1] + terms[-2])

print(sum)