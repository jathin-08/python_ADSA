# Session 04: Variable Sliding Window
# Notes and implementation of Variable Sliding Window.
# File contains class notes and code.
#
#
#
#
#

# Ex: [2,1,5,8,39]
# [2]             Fixed:k=3
# [2,1]           [2,1,5]-->[1,5,8]-->[5,8,39]
# [2,1,5]
# [2,1,5,8]
# [1,5]
# [1,5,8]
# 
# ------
# ------
# 
# Real-World Appl1:
# Meesho Product Purchase app
# 
# Algorithm for Variable Sliding Window:
# Step-1: Two-Pointer Approach
# Step-2: for loop
# Step-3: Expand Window
# Step-4: check with condition
# Step-5: if condition is false
# Step-6: Shrink the window
# step-7: Update the result/Answer
# 
# How to identify, which type of sliding window will be used in problem-solving
# Sliding window concepts are mainly used in Sub-arrays or Sub-strings
# 
# Fixed:                          Variable:
# 1. Size of K                    1. Almost of K
# 2. Length of K                  2. Almost of K
#                                 3. Minimum or Maximum of K
#                                 4. Less than or equal & greater than or equal to K

#Find the longest Sub-array with sum is less than or equal to K?

def longest_subarray(arr, k):
    left = 0
    current_sum = 0
    max_len = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum > k:
            current_sum -= arr[left]
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    return max_len

if __name__ == "__main__":
    arr = [2, 1, 5, 8, 39]
    k = 10
    print("Array:", arr)
    print("K:", k)
    print("Longest sub-array length:", longest_subarray(arr, k))
