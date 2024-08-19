import random

target_number = random.randint(1, 100)
user_guess = None

while user_guess != target_number:
    user_guess = int(input("Guess the number between 1 and 100: "))
    if user_guess < target_number:
        print("Too low, try again.")
    elif user_guess > target_number:
        print("Too high, try again.")
    else:
        print("Congratulations! You've guessed the correct number.")
