import random

guessedNumber = int(input("Guess the number (You have 5 chances): "))

n = random.randint(1, 9)

chances = 0

if(guessedNumber == n):
    print("You guessed the correct number!")
else:
    chances = chances-1
    print("Wrong Number. TRY AGAIN!")
    print("You have", chances, "chances")
