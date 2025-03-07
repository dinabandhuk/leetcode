# 334. Increasing Triplet Subsequence
# Medium
# Topics
# Companies

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.

# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.

# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

 

# Constraints:

#     1 <= nums.length <= 5 * 105
#     -231 <= nums[i] <= 231 - 1

 
# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 747.8K
# Submissions
# 1.9M
# Acceptance Rate
# 39.2%
# Topics
# Array
# Greedy

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num<=first:
                first = num
            elif num<=second:
                second = num
            else:
                return True
        return False

print(Solution.increasingTriplet(Solution, [20,100,10,12,5,13]))


# this fails test cases because it checks for consecutive only but there is no such constraint
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        i,j,k = 0,0,0
        for i in range(0, len(nums)-2):
            j = i+1
            k = j+1
            print(nums[i], nums[j], nums[k])
            if nums[i] < nums[j] < nums[k]:
                return True
        return False
            
