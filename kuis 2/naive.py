# Bubble Sort (Naive Sorting)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_bubble = bubble_sort(numbers[:])

print("\nSorted Numbers (Bubble Sort):")
print(sorted_bubble)
