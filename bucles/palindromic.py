
#problema de la comparacion
n = int(input())
copia_n = n
palindromo = True
divisor = 1
while n//divisor > 9: 
    divisor *= 10

while divisor > 1 and palindromo:
    primer_digito = n//divisor
    ultimo_digito = n%10
    if ultimo_digito != primer_digito:
        palindromo = False
    print(primer_digito, ultimo_digito)
    n = n - primer_digito*divisor
    n = n // 10
    print(n) 
    divisor //= 100

if palindromo:
    print("Es palindromo")
else:
    print("No es palindromo")

n = copia_n
palindromo = True
invertido = 0

while n > 0:
    invertido = invertido*10 + n%10
    n //= 10

if invertido == copia_n:
    print("Es palindromo")
else:
    print("No es palindromo")
    
print(invertido)