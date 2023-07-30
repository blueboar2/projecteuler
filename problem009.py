for i in range(1, 1001):
    for j in range(i, 1001 - i + 1):
        k = 1000 - i - j

        if not(j > i and k > j):
            continue

        if i*i + j*j == k*k:
            print(i, '^2 + ', j, '^2 = ', k, '^2', sep='')
            print(i*j*k)
