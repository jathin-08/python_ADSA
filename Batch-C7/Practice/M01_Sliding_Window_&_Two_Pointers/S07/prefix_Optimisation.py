from typing import List

'''
Prefix : Start from the begining of the array elem up to the current index

Ex: [1,2,3,4,5]

Prefix[0] = [0]
Prefix[1] = [1,2]
Prefix[2] = [1,2,3]
Prefix[3] = [1,2,3,4]
Prefix[4] = [1,2,3,4,5]

Prefix_sum :
Prefix_sum[0] = 0
Prefix_sum[1] = 1
Prefix_sum[2] = 3
Prefix_sum[3] = 6
Prefix_sum[4] = 10

Formula:
Prefix[i] = prefix[i-1] + nums[i]    (i > 0)

Why we use Prefix :
Suppose, i want to calculate the sum(L,R) :
Without Prefix : We have to calculate the sums everytime-->(O(n**2))
With Prefix : First we find the total sum -->O(1)

Formula:
Sum(L,R) = prefix[R+1] - prefix[L]
(or)
Sum(L,R) = prefix[R] - prefix[L-1]

diff btw:
   Sliding Window                                     Prefix 
1. It contains only +ve elem                       1. It have both +ve & -ve
2. window Size is either fixed or extend           2. Exact count
and shrink

'''
#Leet code : 724
#Pivot index:
#Sum of all the leftmost elem == Sum of all the rightmost elem

'''Algorithm:
1. Total Sum
2. initial value of left sum
3. traverse all array elem
4  find the right_sum
5. if left_sum == right_sum
6. return the current index
7. update left_sum
8. return -1
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Total_sum = sum(nums)
        Left_sum = 0
        for i in range(len(nums)):
            right_sum = Total_sum - Left_sum - nums[i]
            if Left_sum == right_sum:
                return i
            Left_sum += nums[i]
        return -1
        
#Leet code : 1991
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        Total_sum = sum(nums)
        Left_sum = 0
        for i in range(len(nums)):
            Right_sum = Total_sum - Left_sum - nums[i] 
            if Left_sum == Right_sum:
                return i
            Left_sum += nums[i]
        return -1


#Leet code : 1732
'''
Algorithm : 
1) Curr_alti = 0
2) Iniital value high_alti = 0
3) Traverse your elements
4) Update Curr_alti
5) Calculate the maximum of high_alti
6) return Maxi of high_alti
'''

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_alti = 0
        maxi_alti = 0
        for change in gain:
            cur_alti += change
            maxi_alti = max(maxi_alti, cur_alti)
        return maxi_alti


        
#Leet code : 2574