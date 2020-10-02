def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)): 

        if arr[i] == target: 
            return i 

    return -1   # not found


# Write an iterative implementation of Binary Search
# It returns index of "target" in given array arr if present, 
# else returns -1 
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high: 
  
        mid = (high + low) // 2
  
        # Check if target is present at mid 
        if arr[mid] < target: 
            low = mid + 1
  
        # If target is greater, ignore left half 
        elif arr[mid] > target: 
            high = mid - 1
  
        # If target is smaller, ignore right half 
        else: 
            return mid 
  
    # If we reach here, then the element was not present

    return -1  # not found
