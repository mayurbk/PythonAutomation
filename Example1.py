#Guess the number game:
import random
x = dir(random)
print(x)
secretNumber = random.randint(1,20)
print("There is a number between 1 and 20. You need to guess the number in 3 attempts!")

#Asking the player to guess the number in 3 attempts.
for guessNo in range(1,4):
    print("Guess the number !")
    guess = int(input())

    #condition of the game
    if guess < secretNumber:
        print("Your guess is too low! Try with a greater number.")
    elif guess > secretNumber:
        print("Your guess is too high ! Try with a lower number.")
    else:
        break
if guess == secretNumber:
    print("Great ! You have correctly guessed the number.The number is ", secretNumber)
else:
    print("Attempt finished. The number is ", secretNumber)