n = int(input())
base = 8
conversion = 0
mul = 1
while n > 0:
    res = n%base
    n = n//base
    conversion += res*mul
    mul *= 10
print(conversion)