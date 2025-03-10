celsius_inicial = int(input())
celsius_final = int(input())

farenheit_inicial = int(celsius_inicial*9/5 + 32)
farenheit_final = int(celsius_final*9/5 + 32)

print("Temperatura en Farenheit")
for i in range(farenheit_inicial, farenheit_final + 1):
    print(i)

