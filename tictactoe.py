import random
import time
from os import system,name

def clrscr():        
    if name =='nt':              #clear screen code for windows
        _= system('cls')
    else:                        #clear screen code for mac 
        _=system('clear')

def insertletter(let,pos):
    board[pos]=let

def isfree(pos):
    return board[pos]==' '

def printboard():
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print(" " + board[7] + " | " + board[8] + " | " + board[9])

def isfull(board):
    if(board.count(' ')>1):
        return False
    else:
        return True

def winner(b,l):
    return ((b[1] == l and b[2]==l and b[3]==l) or (b[4] == l and b[5]==l and b[6]==l) or (b[7] == l and b[8]==l and b[9]==l) or (b[1] == l and b[4]==l and b[7]==l) or (b[2] == l and b[5]==l and b[8]==l) or (b[3] == l and b[6]==l and b[9]==l)or (b[1] == l and b[5]==l and b[9]==l) or (b[3] == l and b[5]==l and b[7]==l))

def player(x,name):                #player's move
    run = True
    while(run):
        move = input(name+" your turn\nPlease select a position to enter \'"+x+"\' between (1 - 9):")
        try:
            move = int(move)
            if move > 0 and move <10:
                if isfree(move):
                    run = False
                    insertletter(x,move)
                else:
                    print("Sorry this space is occupied. choose another position.")
            else:
                print("Please enter a valid position!!")
        except:
            print("Please type a number!!")

def pc():                          #computer's move
    possiblemove = [x for x , letter in enumerate(board) if letter == ' ' and x!= 0 ]
    move = 0
    if possiblemove == []:
        return move
    else:
        for let in ['0','X']:
            for i in possiblemove:
                boardcopy = board[:]
                boardcopy[i] = let
                if winner(boardcopy, let):
                    move = i
                    return move
        corner = []
        for i in possiblemove:
            if i in [1,3,7,9]:
                corner.append(i)
    
        if len(corner)>0:
            move = random.randint(0,len(corner)-1)
            return corner[move]
    
        edge=[]
        for i in possiblemove:
            if i in [2,4,6,8]:
                edge.append(i)
    
        if len(edge)>0:
            move = random.randint(0,len(edge)-1)
            return edge[move]

def withpc():                     #single player game with AI
    nam=input("Enter your name:")
    print("Welcom ",nam,"\nLet's start the game!")
    time.sleep(1.5)
    global board
    board = [" " for x in range(10)]
    printboard()
    while not(isfull(board)):
        if not(winner(board, '0')):
            clrscr()
            printboard()
            time.sleep(0.5)
            player("X",nam)
            clrscr()
            printboard()
            time.sleep(0.5)
        else:
            clrscr()
            printboard()
            time.sleep(0.5)
            print("Sorry you loose")
            time.sleep(0.5)
            break
        
        if not(winner(board,'X')):
            move = pc()
            if move == 0:
                break
            else:
                insertletter('0',move)

        else:
            clrscr()
            printboard()
            print("You win")
            time.sleep(0.5)
            break
    
    if isfull(board):
        clrscr()
        printboard()
        time.sleep(0.5)
        print("Tie game")
        time.sleep(0.5)

def withplayer():                  #multi player game
    p1=input("player 1 Enter your name:")
    p2=input("player 2 Enter your name:")
    clrscr()
    print("Welcom ",p1," and ",p2,"\nLet's start the game!")
    time.sleep(1.5)
    global board
    board = [" " for x in range(10)]
    pl1="X"
    pl2="0"
    while not(isfull(board)):
        if not(winner(board, pl2)):
            clrscr()
            printboard()
            time.sleep(0.5)
            player(pl1,p1)
            clrscr()
            printboard()
            time.sleep(0.5)
        else:
            clrscr()
            printboard()
            time.sleep(0.5)
            print(p2," you won the game")
            time.sleep(0.5)
            break

        if(not(isfull(board))):
            if not(winner(board,pl1)):
                clrscr()
                printboard()
                time.sleep(0.5)
                player(pl2,p2)
                clrscr()
                printboard()
                time.sleep(0.5)
            else:
                clrscr()
                printboard()
                time.sleep(0.5)
                print(p1," you won the game")
                time.sleep(0.5)
                break
    
    if isfull(board):
        clrscr()
        printboard()
        time.sleep(0.5)
        print("Tie game")
        time.sleep(0.5)

while(True):
    clrscr()
    print("---Welcome to tic-tac-toe---")
    print("1.Single Player")
    print("2.Multi Player")
    z=input("Choose Mode(1 or 2):")
    try:
        z=int(z)
        if(z==1):
            clrscr()
            withpc()
        elif(z==2):
            clrscr()
            withplayer()
        else:
            print("Please enter 0 or 1")
            time.sleep(0.5)
            continue
    except:
        print("Please enter a number")
        time.sleep(0.5)
        continue
    y=input("Do you want to play again(y or n):").lower()
    if(y == 'y'):
        continue
    else:
        print("Thank You for playing JJ's game!!!")
        input("Press enter for exit")
        exit()
