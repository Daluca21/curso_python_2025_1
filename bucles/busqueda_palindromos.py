n = int(input())
palindromo = True
divisor = 1 # 10^0
while n//divisor > 9:
    divisor *= 10

while divisor > 1:
    a = n//divisor #digito posicion mayor
    b = n%10 #digito posicion menor
    if a != b:
        palindromo = False
    print(a, b)
    n = n - a*divisor #quito el digito mayor 
    n = n // 10 #quito el digito menor
    divisor //= 100

if palindromo:
    print("Es palindromo")
else: 
    print("No es palindromo")

n = int(input())
a = n
m = 0
while a > 0:
    m = m*10 + a%10
    a //= 10

palindromo = m == n
if palindromo:
    print("Es palindromo")
else: 
    print("No es palindromo")