# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random
total_rolls=0
def roll_dice():
    die1= random.randint(1, 6)
    die2= random.randint(1, 6)
    print(F"Die 1: {die1}, Die 2: {die2}")
    total_rolls=1
    print(f"(Inside function) total_rolls = {total_rolls}")

for i in range(3):
    print(f"/nRoll#{i+1}")
    roll_dice()
    print(f"(Outside function) total_rolls = {total_rolls}")
