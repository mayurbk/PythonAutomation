#creating rock paper scissor game.
import random, sys

print("Welcome to the game of Rock,Paper and Scissors!!!")

#keeping track of the winning , loses and ties.
wins = 0
loses = 0
ties = 0

#Main Game loop starts here

while True:
    print('%s Wins, %s Losses , %s Ties'%(wins,loses,ties))
    while True: #the player will input here
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playermove = input()
        if playermove == 'q':
            print("Sorry to see you go !")
            sys.exit() #Quit the program here
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break  ##come out of player loop
        print('Type one of r,p,s or q')

##Display the player moves
    if playermove == 'r':
        print('ROCK versus ....')
    elif playermove == 'p':
        print('PAPER versus ....')
    elif playermove == 's':
        print('SCISSOR versus ....')

## Display computer moves
    randomMoves = random.randint(1,3)
    if randomMoves == 1:
        computerMove = 'r'
        print('Computer input is ROCK')
    elif randomMoves == 2:
        computerMove = 'p'
        print('Computer input is PAPER')
    elif randomMoves == 3:
        computerMove = 's'
        print("Computer input is SCISSORS")

##Calculate and display record
    if playermove == computerMove:
        print("This is a tie !!")
        ties = ties+1
    elif playermove == 'r' and computerMove == 's':
        print("Hurrah ! You win")
        wins = wins+1
    elif playermove == 'r' and computerMove == 'p':
        print("Phew!! You Lose")
        loses = loses+1
    elif playermove == 'p' and computerMove == 'r':
        print("Hurrah! You win")
        wins = wins+1
    elif playermove == 's' and computerMove == 'p':
        print("Hurrah ! You win")
        wins = wins+1
    elif playermove == 'p' and computerMove == 's':
        print("Phew ! You lose")
        loses = loses+1
    elif playermove == 's' and computerMove =='r':
        print("Phew !! You lose")
        loses = loses+1

