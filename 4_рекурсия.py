def F(n):
    global k
    k += n + 1
    if n > 1:
        k += 2 * n
        F(n - 1)
        F(n - 3)


i = 0
while True:
    k = 0
    i += 1
    F(i)
    if k > 1_000_000:
        print(i, k)
        k = 0
        break

