import random
lista_a = []
for i in range(10):
    lista_a.append(random.randint(1, 5))

lista_b = []
for i in range(10):
    lista_b.append(random.randint(1, 5))

print("Lista A: ", lista_a)
print("Lista B: ", lista_b)


lista_c = []
for i in range(len(lista_a)):
    lista_c.append(lista_a[i])
    lista_c.append(lista_b[i])

print("Lista C: ", lista_c)

lista_c = []
longitud_maxima = len(lista_a)
if len(lista_b) > longitud_maxima:
    longitud_maxima = len(lista_b)


for i in range(longitud_maxima):
    if len(lista_a) > i:
        lista_c.append(lista_a[i])
    if len(lista_b) > i:
        lista_c.append(lista_b[i])

print("Lista C: ", lista_c)
