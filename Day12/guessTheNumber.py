import art
import random

Try = 10

pcChoise = random.randint(1,100)

print(art.logo)

def game(dificulty, guess,Try):

    while Try > 0:
        if guess == pcChoise:
            print(f"{art.win}\nYou guessed the number")
            break
        elif guess > pcChoise:
            Try -= 1
            if Try == 0:
                break
            print("Too high\nGuess again.")
            guess = int(input(f"You have {Try} attempts remaining to guess the number.\nMake a guess: "))
        elif guess < pcChoise:
            Try -= 1
            if Try == 0:
                print("You've run out of guesses. Refresh the page to run again.")
                break
            print("Too low\nGuess again.")
            guess = int(input(f"You have {Try} attempts remaining to guess the number.\nMake a guess: "))



dificulty = input("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100. Choose a difficulty. Type 'easy' or 'hard':").lower()
if dificulty == "hard":
    Try = 5
guess = int(input(f"You have {Try} attempts remaining to guess the number.\nMake a guess: "))

game(dificulty, guess, Try)

