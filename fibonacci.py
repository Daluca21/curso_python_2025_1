#Imprime el fibonacci número n https://oeis.org/A000045

n = int(input())
fibo_i = 0
fibo_j = 1
for it in range(0, n-1):
    fibo_k = fibo_j + fibo_i
    fibo_j = fibo_i
    fibo_i = fibo_k
print(fibo_i)