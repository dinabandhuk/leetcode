# 1679. Max Number of K-Sum Pairs
# Medium
# Topics
# Companies
# Hint

# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

 

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.

 

# Constraints:

#     1 <= nums.length <= 10^5
#     1 <= nums[i] <= 10^9
#     1 <= k <= 10^9

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        count = 0
        
        while left < right:
            s = nums[left] + nums[right]
            if s == k:
                count += 1
                left += 1
                right -= 1
            elif s < k:
                left += 1
            else:
                right -= 1
                
        return count
                
        
        
print(Solution.maxOperations(Solution,  [3,1,3,4,3], 6))