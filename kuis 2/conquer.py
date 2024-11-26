import random

# Generate random integers
random.seed(40)
numbers = [random.randint(0, 1000) for _ in range(50)]

# Merge Sort using Divide and Conquer
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer and merge
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Compare elements and merge
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append remaining elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

# Perform sorting
sorted_numbers = merge_sort(numbers)

print("Original Numbers:")
print(numbers)
print("\nSorted Numbers (Merge Sort):")
print(sorted_numbers)
