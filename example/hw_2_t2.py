n = 10

for count in range(1, n, 2):
    print(" " * int(n - count / 2) + "*" * count)

print(" " * (n - 1) + "*")