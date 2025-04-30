# Milestone #1: Mars Weight

# Prompt user for their weight on Earth
earth_weight = float(input("Enter a weight on Earth: "))

# Calculate the equivalent weight on Mars (37.8% of Earth's weight)
mars_weight = earth_weight * 0.378

# Print the result rounded to 2 decimal places
print(f"The equivalent on Mars: {round(mars_weight, 2)}")

# Milestone #2: Adding in All Planets

# Create a dictionary that maps planets to their gravitational constants
planet_gravity = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Prompt user for their weight on Earth
earth_weight = float(input("Enter a weight on Earth: "))

# Prompt user for the planet they want to calculate weight for
planet = input("Enter a planet: ")

# Check if the planet entered is valid
if planet in planet_gravity:
    # Calculate the weight on the selected planet
    planet_weight = earth_weight * planet_gravity[planet]
    # Print the result rounded to 2 decimal places
    print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}")
else:
    print("Invalid planet name! Please enter a valid planet.")
