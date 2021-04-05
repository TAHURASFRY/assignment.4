import termcolor2
m = int(input())
n = int(input())

for _ in range(0 , n):
    if _ % 2 == 0:
        for _ in range(0 , m):
            if _ % 2 == 0:
                 print(termcolor2.colored("$", color="yellow") , end=' ')
            elif _ % 2 == 1:
                print(termcolor2.colored("@", color="red") , end =' ')
        print()
    if _ % 2 == 1:
        for _ in range(0 , m):
            if _ % 2 == 1:
                print(termcolor2.colored("$", color="yellow") , end=' ')
            elif _ % 2 == 0:
                print(termcolor2.colored("@", color="red") , end =' ')
        print()
