n = int(input())
euler = 0

for i in range(n):
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    euler += 1/factorial
print(euler)

euler = 1
factorial = 1
for j in range(1, n):
    factorial *= j
    euler += 1/factorial

print(euler)