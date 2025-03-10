a = 15
if a > 0:
    print("a es positivo")
    if a == 14:
        print("a es 15")
    print("fin del ifmn")
elif a == 0:
    print("a es cero")
elif a < 0:
    print("a es negativo")
print("fin del ifmy")

#nota = float(input())
nota = 10
if nota <= 10 and nota > 9:
    print("S")
elif nota <= 9 and nota > 8:
    print("A")
elif nota <= 8 and nota > 7:
    print("B")
elif nota <= 7 and nota > 6:
    print("C")
elif nota <= 6 and nota >= 0:
    print("D")
else:
    print("nota no es valida")



#imprimir 10 veces hola
a = 0
while a < 10:
    #print("hola")
    a = a + 1

for i in range(0, 10):
    #print(i)
    pass

suma = 0
n = 12345
while n > 0:
    ultimo_digito = n%10 #acceder/obtener
    suma = suma*10 + ultimo_digito #sumar
    n = n//10 #quitar
print(suma)