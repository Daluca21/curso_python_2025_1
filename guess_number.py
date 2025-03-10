import random
num = random.randint(1, 50)
print("num es", num)
looking_for = True
while looking_for:
    a = int(input())
    if num > a:
        print("El numero es mayor")
    elif num < a:
        print("El numero es menor")
    else: 
        looking_for = False
        print("Es ese el numero")

num = random.randint(1, 50)
print("num es", num)
looking_for = True
for i in range(0, 5):
    a = int(input())
    if num > a:
        print("El numero es mayor")
    elif num < a:
        print("El numero es menor")
    else: 
        looking_for = False
        print("Es ese el numero")
        break

if looking_for:
    print("numero no adivinado")
