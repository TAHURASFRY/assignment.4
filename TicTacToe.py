import termcolor2
import random
import time


def show():
    for i in range (3):
        print()
        for j in range (3):
            print(game[i][j], end=' ')

game = [['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']]

show()

def chek1():
    for i in range(3):
        if game[i][0] == (termcolor2.colored('X', color="green")) and game[i][1] == (termcolor2.colored('X', color="green")) and game[i][2] == (termcolor2.colored('X', color="green")):
         print(termcolor2.colored('\nPlayer 1 wins!', color="yellow"))
         exit()

    for j in range(3):
        if game[0][j] == (termcolor2.colored('X', color="green")) and game[1][j] == (termcolor2.colored('X', color="green")) and game[2][j] == (termcolor2.colored('X', color="green")):
         print(termcolor2.colored('\nPlayer 1 wins!', color="yellow"))
         exit()
    if game[0][0] == (termcolor2.colored('X', color="green")) and game[1][1] == (termcolor2.colored('X',color="green")) and game[2][2] == (termcolor2.colored('X', color="green")):
        print(termcolor2.colored('\nPlayer 1 wins!', color="yellow"))
        exit()

    if game[0][2] == (termcolor2.colored('X', color="green")) and game[1][1] == (termcolor2.colored('X', color="green")) and game[2][0] == (termcolor2.colored('X', color="green")):
        print(termcolor2.colored('\nPlayer 1 wins!', color="yellow"))
        exit()

def chek2():
    for i in range (3):
        if game[i][0] == (termcolor2.colored('O', color="blue")) and game[i][1] == (termcolor2.colored('O', color="blue")) and game[i][2] == (termcolor2.colored('O', color="blue")):
         print(termcolor2.colored('\nPlayer 2 wins!', color="yellow"))
         exit()

    for j in range (3):
        if game[0][j] == (termcolor2.colored('O', color="blue")) and game[1][j] == (termcolor2.colored('O', color="blue")) and game[2][j] == (termcolor2.colored('O', color="blue")):
         print(termcolor2.colored('\nPlayer 2 wins!', color="yellow"))
         exit()
    
    if game[0][0] == (termcolor2.colored('O', color="blue")) and game[1][1] == (termcolor2.colored('O', color="blue")) and game[2][2] == (termcolor2.colored('O', color="blue")):
         print(termcolor2.colored('\nPlayer 2 wins!', color="yellow"))
         exit()

    if game[0][2] == (termcolor2.colored('O', color="blue")) and game[1][1] == (termcolor2.colored('O', color="blue")) and game[2][0] == (termcolor2.colored('O', color="blue")):
        print(termcolor2.colored('\nPlayer 2 wins!', color="yellow"))
        exit()

while True:
    print()
    print("\nPlayer 1")
    while True:
        row = int(input())
        col = int(input())

        if 0 <= row <= 2 and 0 <= col <=2:
           if game[row][col] == '_':
             game[row][col] = (termcolor2.colored('X', color="green"))
             break
           else:
               print(termcolor2.colored('Erroe!This cell has been taken.', color="red"))
        else:      
            print(termcolor2.colored('Error!Index out of range. Try again.', color="red"))
     
    show()
    chek1()

    print()
    print("\nPlayer 2")
    while True:
        row = int(input())
        col = int(input())
        if 0 <= row <= 2 and 0 <= col <=2:
            if game[row][col] == '_':
             game[row][col] = (termcolor2.colored('O', color="blue"))
             break
            else:
                print(termcolor2.colored('Erroe!This cell has been taken.', color="red"))
        else:      
            print(termcolor2.colored('Error!Index out of range. Try again.', color="red"))
            

    show()
    chek2()

    
        
