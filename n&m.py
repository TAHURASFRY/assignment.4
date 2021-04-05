m = int(input())
n = int(input())

for _ in range(0 , n):
    if _ % 2 == 0:
        for _ in range(0 , m):
            if _ % 2 == 0:
                 print("$" , end=' ')
            elif _ % 2 == 1:
                print("@" , end =' ')
        print()
    if _ % 2 == 1:
        for _ in range(0 , m):
            if _ % 2 == 1:
                print("$" , end=' ')
            elif _ % 2 == 0:
                print("@" , end =' ')
        print()
