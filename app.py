import random

def number_guessing_game(static_number):
    attempts = 3
    print("Welcome to the Number Guessing Game!")
    print("You have 3 attempts to guess a 2-digit number.")
     # print(f"The static number is: {static_number}")

    while attempts > 0:
        guess = input("Enter your guess (a 2-digit number): ")

        # Validate the input
        if len(guess) != 2 or not guess.isdigit():
            print("Invalid input. Please enter a 2-digit number.")
            continue
        
        guess = int(guess)

        if guess == static_number:
            print("Congratulations! You've guessed the number correctly!")
            break
        else:
            attempts -= 1
            print(f"Incorrect guess. You have {attempts} attempts remaining.")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct number was {static_number}.")

# Set a static number for the game
static_number = 20  # You can change this to any 2-digit number
number_guessing_game(static_number)