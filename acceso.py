nivel = int(input())
llave = input()
coins = int(input())

if (nivel >= 10 and llave == "S") or coins >= 500:
    print("Acceso permitido")
else:
    print("No permitido")

if (nivel >= 10 and llave == "S"): 
    print("Acceso permitido")
elif coins >= 500:
    print("Acceso permitido")
else:
    print("No permitido")


if (nivel < 10 or llave != "S") and coins < 500:
    print("No permitido")
else:
    print("Acceso permitido")
