n = int(input())
factorial = 1
for i in range(1, n+1): #1 .. n
    
    factorial = factorial*i
factorial = 1
while n > 0:
    factorial = factorial*n
    n -= 1

print(factorial)