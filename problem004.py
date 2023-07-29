x = 0
y = 0
largest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        res = i * j
        sres = str(res)
        ores = ""
        for k in range(1, len(sres) + 1):
            ores = ores + sres[-k]
        if sres == ores and res > largest:
            largest = res
            x = i
            y = j

print(x, "*", y, "=", largest)