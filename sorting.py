import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Arrays
A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
B = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]

# Measure time and sort using Bubble Sort
start_time = time.perf_counter()
sorted_A_bubble = A.copy()
bubble_sort(sorted_A_bubble)
end_time = time.perf_counter()
bubble_time_A = end_time - start_time

start_time = time.perf_counter()
sorted_B_bubble = B.copy()
bubble_sort(sorted_B_bubble)
end_time = time.perf_counter()
bubble_time_B = end_time - start_time

# Measure time and sort using Quick Sort
start_time = time.perf_counter()
sorted_A_quick = quick_sort(A.copy())
end_time = time.perf_counter()
quick_time_A = end_time - start_time

start_time = time.perf_counter()
sorted_B_quick = quick_sort(B.copy())
end_time = time.perf_counter()
quick_time_B = end_time - start_time

# Output results
print("Bubble Sort Results:")
print(f"Sorted A: {sorted_A_bubble}, Time: {bubble_time_A:.6f} seconds")
print(f"Sorted B: {sorted_B_bubble}, Time: {bubble_time_B:.6f} seconds")

print("\nQuick Sort Results:")
print(f"Sorted A: {sorted_A_quick}, Time: {quick_time_A:.6f} seconds")
print(f"Sorted B: {sorted_B_quick}, Time: {quick_time_B:.6f} seconds")

# Penjelasan No.2 
#Quick Sort lebih efektif untuk kasus A dan B dikarenakan kompleksitas waktu rata-rata yang lebih rendah serta memiliki efisiensi yang lebih tinggi untuk data set yang besar dan dapat bekerja dengan baik pada data yang tidak terurut maupun terurut.