n = int(input())
for a in range(1, n+1):
    suma = 0
    for i in range(1, a): # 1 .. a-1
        if a%i == 0:
            suma += i
    if suma == a:
        print(a, "es perfecto")
