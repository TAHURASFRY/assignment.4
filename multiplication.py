m = int(input())
n = int(input())

rows = n
columns = m

for i in range(1, 1+m):
    print()
    for j in range(1, 1+n):
        print(i*j, end=' ')
