n = int(input())
divisor = 2
while n > 1:
    while n%divisor != 0 and divisor <= n:
            divisor += 1
            
    while n%divisor == 0:
        n /= divisor
        print(divisor)
    

