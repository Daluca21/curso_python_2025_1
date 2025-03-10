xp = int(input())
if xp >= 700:
    xp = xp*11/10 #Aplica el bono

print(xp)
if xp >= 0 and xp <= 100:
    print("novato")
elif xp <= 500:
    print("aprendiz")
elif xp <= 1000:
    print("veterano")
else:
    print("maestro")