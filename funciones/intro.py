
def saludar():
    print("Hola")

import random

def rotar(lista):
    lista_copia = lista.copy()
    primer_elemento = lista[0]
    print(lista)

    for i in range(len(lista) - 1):
        lista_copia[i] = lista[i+1]

    lista_copia[-1] = primer_elemento
    return lista_copia

def generar_lista_aleatoria(n = 10, l = 1, r = 5):
    lista = []
    print("n:", n, "l:", l, "r:", r)
    for i in range(n):
        lista.append(random.randint(l, r))
    return lista


n = 10
l = 0
r = 10
#generar una lista de numeros aleatorios

lista = []
for i in range(n):
    lista.append(random.randint(l, r))
lista2 = []
for i in range(n):
    lista2.append(random.randint(l, r))
lista3 = []
for i in range(n):
    lista3.append(random.randint(l, r))
lista4 = []
for i in range(n):
    lista4.append(random.randint(l, r))
lista5 = []
for i in range(n):
    lista5.append(random.randint(l, r))
lista6 = []
for i in range(n):
    lista6.append(random.randint(l, r))


def sumar(a = 0, b = 0):
    return a + b


def aproximar_euler(n = 1):
    euler = 0
    for i in range(n):
        factorial = 1
        for j in range(1, i+1):
            factorial *= j
        euler += 1/factorial
    return euler

def promediar_sin_extremos(lista):    
    mn = min(lista)
    mx = max(lista)
    suma = sum(lista)
    promedio = (suma - (mx + mn))/(len(lista) - 2)
    return promedio

generar_lista_aleatoria(12, 4) #indico la n, indica la l
generar_lista_aleatoria(19, 1, 20)# indico la n, indico la l, indico la r
generar_lista_aleatoria(15) #indico la n
generar_lista_aleatoria() 
generar_lista_aleatoria(r = 14, n = 9) #indico la n , indico la r
generar_lista_aleatoria(r = 10, l = -2, n = 131)

print(sumar())
print(sumar(5, 4))
print(sumar(3))
print(sumar(b= 2, a = 6))
print(sumar(b=2))
print(sumar(a=6))

lista_aleatoria = generar_lista_aleatoria()
for i in range(5):
    lista_aleatoria = rotar(lista_aleatoria)

print(aproximar_euler(3))
print(promediar_sin_extremos(lista_aleatoria))


i = -10

def calcular():
    global i
    i = 0
    while(i < 10):
        print(i)
        i += 1

def calcular2():
    global i
    while(i < 10):
        print(i)
        i += 1

calcular()
calcular2()
