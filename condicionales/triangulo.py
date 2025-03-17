a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print("Triangulo valido")
    if a == b and b == c:
        print("Equilatero")
    elif (a != b and a != c and b != c):
        print("Escaleno")
    else:
        print("Isosceles")
else:
    print("Triangulo no es valido")