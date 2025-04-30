import random

# Constant for number of rounds
NUM_ROUNDS = 5

# Function to play the game
def high_low_game():
    # Initial message
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # Score variable
    score = 0

    # Loop through rounds
    for round_number in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_number}")

        # Generate random numbers for you and the computer
        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        # Display your number (computer's number is hidden)
        print(f"Your number is {your_number}")

        # Get user's guess (higher or lower)
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Validate user input
        while guess not in ['higher', 'lower']:
            guess = input("Please enter either 'higher' or 'lower': ").lower()

        # Compare numbers and check if the guess is correct
        if (guess == 'higher' and your_number > computer_number) or (guess == 'lower' and your_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1  # Increment score for correct guess
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        # Print the score after each round
        print(f"Your score is now {score}")

    # Game over - Print final score and performance message
    print("\nThanks for playing!")
    print(f"Your final score is: {score}")

    # Performance evaluation based on score
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Run the game
high_low_game()
