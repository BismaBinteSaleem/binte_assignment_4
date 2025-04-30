import random

def computer_guesses_number():
    print("🤖 Think of a number between 1 and 100, and I will try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = random.randint(low, high)
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it too high (H), too low (L), or correct (C)? ").strip().upper()

        if feedback == 'C':
            print(f"🎉 Yay! I guessed your number in {attempts} attempts!")
            break
        elif feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
        else:
            print("❌ Please enter H, L, or C only.")

# Run the game
computer_guesses_number()
