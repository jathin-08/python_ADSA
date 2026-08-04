from typing import List

'''
Binary--> 
It contains only 0's and 1's
Ex: 
[1,0,1,0,1,0]
[1]
[1,0]
[1,0,1]
[0]
[0,1]
[1]
[1,1]-->Not a sub-array
-----
-----
-----
'''
#Leetcode : 1493
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left,right = 0, 0
        ans = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                ans += 1
            while ans  > 1:
                if nums[left] == 0:
                    ans -=1
                left += 1
            max_len = max(max_len, right -left + 1)
        return max_len -1

# Save LeetCode 1493 Solution class since class name Solution will be redefined below
Solution_1493 = Solution
        
#Leet Code : 1004
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right = 0,0
        ans = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                ans +=1
            while ans > k:  
                if nums[left] == 0:
                    ans -=1
                left += 1
            max_len= max(max_len, right-left +1)
        return max_len      

#Leet Code : 930

if __name__ == "__main__":
    # Test LeetCode 1493
    sol_1493 = Solution_1493()
    nums1 = [1, 1, 0, 1]
    print("Running Binary_Subarrays.py...")
    print("=" * 40)
    print("LeetCode 1493 (Longest Subarray of 1's After Deleting One Element):")
    print(f"Input: nums = {nums1}")
    print(f"Output: {sol_1493.longestSubarray(nums1)}")
    print("-" * 40)

    # Test LeetCode 1004
    sol_1004 = Solution()
    nums2 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k2 = 2
    print("LeetCode 1004 (Max Consecutive Ones III):")
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {sol_1004.longestOnes(nums2, k2)}")
    print("=" * 40)
