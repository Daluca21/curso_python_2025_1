lista = [21, 14, 7, 19, 23]

for i in range(5):
    print(lista[i])

for i in range(4, -1, -1): #(4, 0, -1)
    print(lista[i])

for i in range(-1, -6, -1): #(-1, -5, -1)
    print(lista[i])

sublista = lista[:4:2]
print("Elementos sublista")
for i in range(len(sublista)):
    print(sublista[i])

lista = []
lista.append("Daniel")
lista.append("Alejandro")
lista.append("Jose")
lista.append("Daniel")
lista.insert(-1, "Maria")
print(lista)
lista.remove("Daniel")
lista.remove("Daniel")
lista.pop(0)
print(lista)

lista = []

for i in range(10):
    lista.append(2*i)

print(lista)

lista[5] = 100
lista[7] = 200
suma = 0
for i in range(10):
    suma += lista[i]

print(lista)
print(suma)
print(len(lista))
print(max(lista))
print(min(lista))
print(sum(lista))
lista = sorted(lista)
print(lista)
for i in range(len(lista) - 3, len(lista)):
    print(lista[i])

print("Imprimiendo lista")
k = 0
for x in lista:
    print("elemento ",k,":", x)
    k += 1

cuadrados = [x**2 for x in lista]
print(cuadrados)


if 230 in cuadrados:
    print("Esta el 16")

lista = [10, "Nombre"]
print(lista)
for x in lista:
    print(x*10)









