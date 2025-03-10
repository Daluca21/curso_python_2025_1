n = int(input())
prime = True
for i in range(2, n): #2 n-1
    if n%i == 0:
        prime = False   

for i in range(1, n+1): #2 n-1
    if n%i == 0:
        print(i, "es divisor de", n)   


print("Es primo" if prime else "No es primo")

l = int(input())
r = int(input())

for n in range(l, r+1):
    prime = True
    for i in range(2, n):
        if n%i == 0:
            prime = False

    print(n, "Es primo" if prime else "No es primo")