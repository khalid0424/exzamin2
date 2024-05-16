a = input()
k = 2
i = 0
while i < len(a):
    if i == k:
        i += 1
        continue
    print(a[i], end=" ")
    i += 1

print()