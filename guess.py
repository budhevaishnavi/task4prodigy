import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

# Welcome the user and explain the game
print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it!")

# Loop until the user correctly guesses the number
while True:
    # Prompt the user to input their guess
    user_guess = int(input("Enter your guess: "))

    # Increment the number of attempts
    attempts += 1

    # Compare the user's guess to the secret number
    if user_guess < secret_number:
        print("Too low! Try again.")
    elif user_guess > secret_number:
        print("Too high! Try again.")
    else:
        # The user correctly guessed the number!
        print(f" Congratulations! You won in {attempts} attempts.")
        print(f"The secret number was {secret_number}.")
        break
