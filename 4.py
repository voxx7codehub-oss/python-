n = int(input())

even = []
odd = []

for _ in range(n):
    x = int(input())
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

result = even + odd
print(result)
