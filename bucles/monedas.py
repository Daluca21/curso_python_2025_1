i = 0
ultimo_digito = 100                     #limite monedas
n = 142                                 #suma que busco
infinito = 1000000000000000000
cantidad_de_monedas_minima = infinito   #Mejor respuesta ("Infinito" por ahora)
while i < ultimo_digito:
    j = 0
    while j < ultimo_digito:
        k = 0
        while k < ultimo_digito:
            if n == i*13 + j*7 + k*2:                               #monedas {13, 7, 2}
                print(i, j, k, "cantidad de monerdas", i+j+k)

                if i + j + k < cantidad_de_monedas_minima:
                    cantidad_de_monedas_minima = i + j + k          # Mejoro la solucion

            k += 1
        j += 1
    i += 1

if cantidad_de_monedas_minima == infinito:
    print("No se puede")
else:
    print(cantidad_de_monedas_minima)