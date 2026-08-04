# Session 02: Two-Pointer Optimization 2
# This file covers advanced application of the Two-Pointer Approach.
#
# Example Problem: Container With Most Water (LeetCode 11)
# Given n non-negative integers representing an elevation map, find two lines
# that together with the x-axis forms a container containing the most water.

def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_water

if __name__ == "__main__":
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Heights: {heights}")
    print(f"Max water container area: {max_area(heights)}")
