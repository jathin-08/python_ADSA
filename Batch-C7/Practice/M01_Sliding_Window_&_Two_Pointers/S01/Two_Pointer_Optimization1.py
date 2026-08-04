# Session 01: Two-Pointer Optimization 1
# This file covers the basic Two-Pointer Approach.
#
# Two-Pointer Approach:
# Used on sorted arrays/sequences to find pairs or triplets that meet specific criteria.
# Avoids nested loops (O(N^2)) and achieves linear time complexity (O(N)).
#
# Example Problem: Find if there exists a pair in a sorted array that sums to a target.

def has_pair_with_sum(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True, (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return False, None

if __name__ == "__main__":
    arr = [1, 2, 4, 6, 8, 10, 13]
    target = 14
    found, pair = has_pair_with_sum(arr, target)
    print(f"Array: {arr}, Target: {target}")
    print(f"Pair found: {found} -> {pair}")
