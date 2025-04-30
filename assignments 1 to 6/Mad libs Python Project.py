def mad_libs_game():
    print("🎉 Welcome to Mad Libs Game!")
    print("Please answer the following prompts:\n")

    # Collect input from the user
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    emotion = input("Enter an emotion: ")

    # Create the Mad Lib story using f-string
    story = (
        f"\nToday I went to the {place} feeling very {emotion}. "
        f"I saw a {adjective} {noun} that tried to {verb} me! "
        f"It was the most {emotion.lower()} experience of my life!"
    )

    print("\n📖 Here's your Mad Libs story:")
    print(story)

# Run the game
mad_libs_game()
