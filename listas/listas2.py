lista = [21, 14, 7, 19, 23]
lista = [3, 2, 5, 14, 4, 4]
#lista = [0] * 6

print(lista)

for i  in range(0, 6): #[0, 1, 2, 3, 4, 5]
    print("pos", i, ":", lista[i])

print()
for i  in range(-1, -7, -1): #[-1, -2, -3, -4, -5, -6]
    print("pos", i, ":", lista[i])
    
print()
for i  in range(-6, 0): #[-6, -5, -4, -3, -2, -1]
    print("pos", i, ":", lista[i])

#sublista = lista[1:6:3]
#print(sublista)


lista = []
print(lista)
lista.append(5)
print(lista)
lista.append(100)
print(lista)
lista.append(3)
print(lista)
lista.append(2)
print(lista)
lista.insert(-1, 100)
print(lista)


lista.remove(100)
print(lista)

lista.remove(100)
print(lista)

lista.pop(0)
print(lista)


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
for i in range(0, 10):
    suma += lista[i]

print(lista)
print(suma/10)

print("Tamaño", len(lista))
print("Elemento máximo", max(lista))
print("Elemento minimo", min(lista))
print("Suma", sum(lista))
print(sorted(lista), lista)
lista = sorted(lista)

for i in range(len(lista) - 3, len(lista)):
    print(lista[i])


lista.reverse()
print(lista)

for i in range(0, 3):
    print(lista[i])

print("Elementos lista")
for x in lista:
    print(x)

cuadrados = [x**2 for x in lista]
print(cuadrados)

otralista = [x/4 for x in lista]
print(otralista)

multiplosde3 = [x for x in lista if (x) % 3 == 0]
print(multiplosde3)

if 6 in multiplosde3:
    print("Encontrado")
else:
    print("No encontrado")

lista = [10, "palabra", True]

for x in lista:
    print(x*2)