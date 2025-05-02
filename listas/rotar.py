import random
lista = []
for i in range(10):
    lista.append(random.randint(1, 5))

print(lista)

lista_copia = lista.copy()
primer_elemento = lista[0]
for i in range(len(lista) - 1):
    lista_copia[i] = lista[i+1]

lista_copia[-1] = primer_elemento

print(lista_copia)

lista_copia = []
for i in range(1, len(lista)):
    lista_copia.append(lista[i])
lista_copia.append(lista[0])

print(lista_copia)


lista_copia = lista[1:len(lista)]
lista_copia.append(lista[0])
print(lista_copia)