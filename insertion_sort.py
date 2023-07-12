def insertion_sort(arr):
    n = len(arr)

    # Traverse through 1 to n-1 elements
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print(my_list)  # Output: [11, 12, 22, 25, 34, 64, 90]
