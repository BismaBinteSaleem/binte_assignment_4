import random

def guess_my_number():
    # The computer picks a random number between 0 and 99
    number_to_guess = random.randint(0, 99)
    guess = -1  # Initialize guess variable to start the loop

    print("I am thinking of a number between 0 and 99...")

    # Keep asking the user for guesses until they guess correctly
    while guess != number_to_guess:
        # Ask the user for a guess
        guess = int(input("Enter a guess: "))

        # Check if the guess is too high, too low, or correct
        if guess > number_to_guess:
            print("Your guess is too high")
        elif guess < number_to_guess:
            print("Your guess is too low")

    # When the user guesses correctly
    print(f"Congrats! The number was: {number_to_guess}")

# Run the game
guess_my_number()
