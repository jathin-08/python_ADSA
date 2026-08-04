# Session 03: Fixed Sliding Window
# This file covers the concepts of Fixed Sliding Window.
#
# Fixed Sliding Window:
# The size of the window remains constant throughout the execution.
# Useful when we need to find something in all subarrays of size K.
#
# Example Problem: Find the maximum sum of a subarray of size K.

def max_sum_subarray(arr, k):
    if len(arr) < k:
        return 0
        
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window from start to end of array
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    print(f"Array: {arr}, K: {k}")
    print(f"Max sum subarray of size K: {max_sum_subarray(arr, k)}")
