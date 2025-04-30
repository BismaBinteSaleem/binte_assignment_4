import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Function to get user input and generate passwords
def password_generator():
    print("🔒 Welcome to the Password Generator!")
    
    try:
        # Get number of passwords and length of each password from user
        num_passwords = int(input("Enter the number of passwords you want to generate: "))
        password_length = int(input("Enter the length of each password: "))

        print("\nHere are your generated passwords:\n")
        
        # Generate and display the passwords
        for i in range(num_passwords):
            print(f"Password {i+1}: {generate_password(password_length)}")
    
    except ValueError:
        print("❌ Please enter valid numbers for the number of passwords and their length.")

# Run the password generator
password_generator()
