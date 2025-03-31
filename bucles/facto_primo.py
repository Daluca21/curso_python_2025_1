n = int(input())
copia_n = n
d = 2
while n != 1:
    #intente reducir el numero
    while n%d != 0: #d no divida a la n 
        d += 1
    while n%d == 0:
        n //= d
        print(d)
        
n = copia_n
for d in range(2, n+1):
    while n%d == 0:
        n //= d
        print(d)
