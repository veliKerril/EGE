a = 20
b = 30
print(a, b)

a, b = b, a
print(a, b)

temp = a
a = b
b = temp
print(a, b)
