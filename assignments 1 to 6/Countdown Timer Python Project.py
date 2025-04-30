import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_format = f"{mins:02d}:{secs:02d}"
        print(f"Time Left: {timer_format}", end="\r")  # Overwrite line
        time.sleep(1)
        seconds -= 1

    print("\nTime's up! ⏰")

# Ask user to enter time in seconds
try:
    user_input = int(input("Enter countdown time in seconds: "))
    countdown_timer(user_input)
except ValueError:
    print("Please enter a valid number.")
