numero = input()
suma = 0
for digito in numero:
    suma = suma + int(digito)
print("La suma de los digitos es", suma) 

numero = int(numero)
suma = 0
while numero > 0:
    suma = suma + numero%10
    numero = numero//10
print("La suma de los digitos es", suma) 