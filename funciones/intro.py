import random

def saludar():
    print("Hola")
    print("Como estas?")

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

generar_lista_aleatoria(12, 4)
generar_lista_aleatoria(19, 1, 20)
generar_lista_aleatoria(15)
generar_lista_aleatoria()
generar_lista_aleatoria(r = 14, n = 9)

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