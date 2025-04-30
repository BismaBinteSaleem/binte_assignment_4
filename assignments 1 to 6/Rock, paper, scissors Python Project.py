import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    
    return "Computer wins!"

# Main function for the game
def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors! 🚀")

    # List of choices
    choices = ["rock", "paper", "scissors"]

    while True:
        # Get user input
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()

        # Exit condition
        if user_choice == 'exit':
            print("Thanks for playing!")
            break
        
        if user_choice not in choices:
            print("❌ Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Get computer choice randomly
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine and print the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

# Run the game
rock_paper_scissors()
