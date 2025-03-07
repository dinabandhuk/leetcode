# 643. Maximum Average Subarray I
# Easy
# Topics
# Companies

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

 

# Constraints:

#     n == nums.length
#     1 <= k <= n <= 105
#     -104 <= nums[i] <= 104

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 740.3K
# Submissions
# 1.7M
# Acceptance Rate
# 44.7%
# Topics
# Array
# Sliding Window

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = sliding_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            sliding_sum = sliding_sum + nums[i] - nums[i-k]
            if sliding_sum > max_sum:
                max_sum = sliding_sum
        return max_sum/k
    
# 
        
print(Solution.findMaxAverage(Solution, [1,12,-5,-6,50,3], 4))

# this version below is slower because we used max(max_sum, sliding_sum) which is bad for CPU branch prediction. beats only 58%
# no point in replacing sum() with loop because it got even slower
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = sliding_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            sliding_sum = sliding_sum + nums[i] - nums[i-k]
            max_sum = max(max_sum, sliding_sum)
        return max_sum/k