matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

lista_cadenas = [ ["a","d","a","d"], ["f","s","f","s","f"], "hfhfhfh"]

def imprimir_matriz(matriz):
    for i in range(len(matriz)): #recorro las listas
        for j in range(len(matriz[i])): #recorro los elementos
            print(matriz[i][j], end=" ")
        print() 

def sumar_matrices(matrizA, matrizB):
    matrizC = []     
    for i in range(3):
        matrizC.append([0]*3)  #[0]*3 = [0, 0, 0]

    for i in range(3):
        for j in range(3):
            matrizC[i][j] = matrizA[i][j] + matrizB[i][j]
    return matrizC

def obtener_transpuesta(matriz):
    matrizC = [[]]*3
    for i in range(3):
        matrizC[i] = [0]*3

    for i in range(3):
        for j in range(3):
            matrizC[j][i] = matriz[i][j] 

    return matrizC


def multiplicar_arreglos(arregloA, arregloB):
    arregloC = [0]*len(arregloA)
    for i in range(len(arregloA)):
        arregloC[i] = arregloA[i]*arregloB[i]
    return sum(arregloC)


def multiplicar_matrices(matrizA, matrizB):
    matrizC = [[]]*3
    for i in range(3):
        matrizC[i] = [0]*3
    
    for i in range(3):
        for j in range(3):
            matrizC[i][j] = 0
            for k in range(3):
                matrizC[i][j] +=  matrizA[i][k] *matrizB[k][j]

    return matrizC

def multiplicar_matrices(matrizA, matrizB):
    matrizC = [[]]*3
    for i in range(3):
        matrizC[i] = [0]*3
    matrizB = obtener_transpuesta(matrizB)

    for i in range(3):
        for j in range(3):
            matrizC[i][j] = multiplicar_arreglos(matrizA[i], matrizB[j])
    return matrizC


def multiplicar_matrices(matrizA, matrizB):
    matrizC = [[]]*3
    for i in range(3):
        matrizC[i] = [0]*3

    for i in range(3):
        for j in range(3):
            suma = 0 
            for k in range(3):
                suma += matrizA[i][k]*matrizB[k][j]
            matrizC[i][j] = suma
            
    return matrizC

imprimir_matriz(sumar_matrices(matriz1, matriz2))
imprimir_matriz(matriz1)
imprimir_matriz(obtener_transpuesta(matriz1))
imprimir_matriz(multiplicar_matrices(matriz1, matriz2))
