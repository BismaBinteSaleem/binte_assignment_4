def main():
    
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    #
    print("Length of the list:", len(fruit_list))
    
    
    fruit_list.append('mango')
    
    
    print("Updated list:", fruit_list)

main()


# Problem #2: Index Game
def access_element(lst, index):
    """Access an element at the given index."""
    if index < 0 or index >= len(lst):
        return "Index out of range."
    return lst[index]

def modify_element(lst, index, new_value):
    """Modify the element at the given index with a new value."""
    if index < 0 or index >= len(lst):
        return "Index out of range."
    lst[index] = new_value
    return lst

def slice_list(lst, start_index, end_index):
    """Return a sliced portion of the list."""
    if start_index < 0 or end_index > len(lst) or start_index > end_index:
        return "Invalid indices."
    return lst[start_index:end_index]

def game():
    
    sample_list = [10, 'apple', 3.14, 'banana', True]

    print("Welcome to the Index Game!")
    print("Here's the initial list:", sample_list)

    while True:
       
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit")

        operation = input("Enter your choice (1/2/3/4): ")

        if operation == '1':
            # Access an element
            index = int(input("Enter the index to access: "))
            result = access_element(sample_list, index)
            print(f"Accessed element: {result}")
        
        elif operation == '2':
            # Modify an element
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(sample_list, index, new_value)
            print(f"Updated list: {result}")
        
        elif operation == '3':
            # Slice the list
            start_index = int(input("Enter the start index: "))
            end_index = int(input("Enter the end index: "))
            result = slice_list(sample_list, start_index, end_index)
            print(f"Sliced list: {result}")
        
        elif operation == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice! Please select a valid operation.")


game()
