
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.


def main():
    first_number :str= input ("enter the first number: ")
    num1:int= int(first_number)
    second_number :str= input ("enter the second number: ")
    num2:int = int(second_number)

    total_sum:int= num1 + num2
    
    print("the total sum is :",total_sum)

if __name__ == '__main__':
    main()