n = int(input()) # numero cualquiera
suma = 0
for i in range(1, n): # 1 2 3 ... n - 1 
    if n%i == 0:
        suma += i

if suma == n:
    print("numero es perfecto")
else:
    print("numero no es perfecto")