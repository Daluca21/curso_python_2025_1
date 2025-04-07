n = int(input())
invertido = 0

while n > 0:
    invertido = invertido*10
    invertido = invertido + n%10
    n //= 10

suma = 0
potencia = 1
while invertido > 0:
    ultimo_digito = invertido%10
    j = 0
    ultimo_digito_potencia = 1
    
    while j < potencia:
        ultimo_digito_potencia *= ultimo_digito
        j += 1

    suma += ultimo_digito_potencia
    potencia += 1
    invertido //= 10

print(suma)