a = int(input())
b = int(input())
while a != b:
    if b > a:
        c = a
        a = b
        b = c
    a = a - b
print("El MCD es", a)