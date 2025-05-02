import random
lista = []
for i in range(10):
    lista.append(random.randint(1, 5))

print(lista)

mn = 100
for i in range(len(lista)):
    if lista[i] < mn:
        mn = lista[i]

mx = -1
for i in range(len(lista)):
    if lista[i] > mx:
        mx = lista[i]

suma = 0
for i in range(len(lista)):
    suma += lista[i]

suma = suma - (mn + mx)
promedio = suma / (len(lista) - 2)
print("El promedio de la lista sin extremos es: ", promedio)


mn = min(lista)
mx = max(lista)
suma = sum(lista)
promedio = (suma - (mx + mn))/(len(lista) - 2)
print("El promedio de la lista sin extremos es: ", promedio)
