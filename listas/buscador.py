import random
lista = []
for i in range(100):
    lista.append(random.randint(1, 100))

print(lista)

# Contar cuantas veces aparecen los números del 1 al 100 en 
# una lista

for i in range(1, 101):
    contador = 0
    for j in range(len(lista)):
        if lista[j] == i:
            contador += 1
    if contador != 0:
        print("El numero ", i, " se repite ", contador, " veces")   

lista_contador = [0]*101

for i in range(len(lista)):
    pos_a_contar = lista[i]
    lista_contador[pos_a_contar] += 1

for i in range(1, 101):
    if lista_contador[i] != 0:
        print("El numero ", i, " se repite ", lista_contador[i], " veces")