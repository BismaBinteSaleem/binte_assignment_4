# Binary Search - Iterative Version
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f"Checking middle value: {arr[mid]} at index {mid}")
        
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return -1  # Target not found


# Binary Search - Recursive Version
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Base case: not found

    mid = (low + high) // 2
    print(f"Checking middle value: {arr[mid]} at index {mid}")

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


# Test Data
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9

# Iterative Test
print("==== Iterative Binary Search ====")
result_iter = binary_search_iterative(arr, target)
if result_iter != -1:
    print(f"Target {target} found at index {result_iter} using iterative method.")
else:
    print(f"Target {target} not found using iterative method.")

# Recursive Test
print("\n==== Recursive Binary Search ====")
result_rec = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result_rec != -1:
    print(f"Target {target} found at index {result_rec} using recursive method.")
else:
    print(f"Target {target} not found using recursive method.")
