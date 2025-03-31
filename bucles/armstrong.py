
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            ci = i*i*i
            cj = j*j*j
            ck = k*k*k
            numero = i * 100 + j * 10 + k * 1
            if ci + cj + ck == numero:
                print(numero)
         