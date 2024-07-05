import random
secret_number = random.randint(1, 100)
attempts = 0
print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it!")
while True:
    user_guess = int(input("Enter your guess: "))
    attempts += 1
    if user_guess < secret_number:
        print("Too low! Try again.")
    elif user_guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f" Congratulations! You won in {attempts} attempts.")
        print(f"The secret number was {secret_number}.")
        break
