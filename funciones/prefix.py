#Dado un array de números enteros de longitud n, 
#obtener la suma en un rango desde
#la posición l hasta la posición r (l <= r)


lista = [4, 2, 5, 1, 4, 1, 4 , 6, 1, 5, 1]
prefijos = []
preguntas = []

def agregar_preguntas():
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            preguntas.append([i, j])

def sumar_en_rango(l, r):
    suma = 0
    while l <= r:
        suma += lista[l]
        l += 1
    return suma

def sumar_en_rango_for(lista, l, r):
    suma = 0
    for i in range(l, r + 1): # l ----- r
        suma += lista[i]
    return suma

def sumar_en_rango_compresion(lista, l, r):
    auxiliar = lista[l:(r+1)]
    return sum(auxiliar)

def crear_arreglo_prefijos():
    suma = 0
    for i in range(0, len(lista)):
        suma += lista[i]
        prefijos.append(suma)

def sumar_en_rango_prefijo(l, r):
    # [0, 2] = prefijos[2] - prefijos[-1]
    if l == 0:
        return prefijos[r]
    return prefijos[r] - prefijos[l-1]


crear_arreglo_prefijos()
print(prefijos)
agregar_preguntas()

for pregunta in preguntas:
    print(pregunta)
    print("la suma es", sumar_en_rango(pregunta[0], pregunta[1]))
    print("la suma es", 
          sumar_en_rango_prefijo(pregunta[0], pregunta[1]))



#Prefix sum

# [4, 2,  5,  1,  4,  1,  4,  6,  1,  5,  1]

# [4, 6, 11, 12, 16, 17, 21, 27, 28, 33, 34] arreglo de prefijos

# [5, 7] = prefijo[7] - prefijo[5-1]
# [l, r] = prefijo[r] - prefijo[l-1]

# [ ,  ,   ,   ,   ,  1,  4,  6,   ,   ,   ]

# [4, 2,  5,  1,  4,  1,  4,  6]
# [4, 2,  5,  1,  4]

