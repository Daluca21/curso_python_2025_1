n = int(input())
bn = 0
mul = 1
while n > 0:
    print(n%2)
    bn += n%2*mul
    mul *= 10
    n = n//2
print(bn)