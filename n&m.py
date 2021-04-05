m = int(input())
n = int(input())

for j in range(0 , n):
    if j % 2 == 0:
        for i in range(0 , m):
            if i % 2 == 0:
                 print("$" , end=' ')
            elif i % 2 == 1:
                print("@" , end =' ')
        print()
    if j % 2 == 1:
        for i in range(0 , m):
            if i % 2 == 1:
                print("$" , end=' ')
            elif i % 2 == 0:
                print("@" , end =' ')
        print()
