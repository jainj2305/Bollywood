import time
from os import system, name
from winsound import PlaySound,SND_ASYNC   #module for add music

PlaySound("moonlight.wav",SND_ASYNC)  #music file

def clrscr():                 #clear screen function for windows
    _=system('cls')


word = input("Enter movie name for guessing: ").upper()
time.sleep(1)
clrscr()

name = input("Enter your name: ").upper()

print("Hello, " + name, "Time to play 'BOLLYWOOD'!")

print("")

#wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

#creates an variable with an empty value
guesses = ' '

turns = "BOLLYWOOD"

while turns != '':
    time.sleep(1)
    clrscr()
    failed = 0
    for char in word:
        if char in guesses:
            PlaySound("shoot.wav",SND_ASYNC)
            print(char,end='')
        else:
            print(" _",end='')
            failed += 1
    if failed == 0:
        print("\nYou won")
        break
    guess = input("\nguess a character: ").upper()
    guesses += guess[0]

    if guess not in word:
        PlaySound("enemy.wav",SND_ASYNC)
        turn=turns[0:len(turns)-1]
        turns=turn
        if turns == '':
            print('\nYou have no more guesses!!!')
            print("\nYou Loose")
        else:
            print("\nWrong")
            print("\nYou have",turns, 'more guesses')

delay = input("Press ENTER to finish")
