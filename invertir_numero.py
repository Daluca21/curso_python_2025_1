numero = int(input())
numero_invertido = 0
while numero > 0:
    numero_invertido = numero_invertido*10 + numero%10
    numero = numero//10
print("El número invertido es", numero_invertido) 