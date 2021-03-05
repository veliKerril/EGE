def F(n):
    global x
    x += n*n
    if n > 1:
        x += 2 * n + 1
        F(n - 2)
        F(n // 3)


i = 0
while True:
    x = 0
    i += 1
    F(i)
    if x > 3200000:
        print(i, x)
        break
