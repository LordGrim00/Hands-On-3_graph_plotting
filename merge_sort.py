def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Recursively sort the left and right halves
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Merging the sorted halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any elements were left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Test function to check merge sort
def test_merge_sort():
    arr = [5, 2, 4, 7, 1, 3, 2, 6]
    print(f"Original Array: {arr}")
    merge_sort(arr)
    print(f"Sorted Array: {arr}")

if __name__ == "__main__":
    test_merge_sort()