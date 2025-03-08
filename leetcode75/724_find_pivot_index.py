# 724. Find Pivot Index
# Easy
# Topics
# Companies
# Hint

# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

 

# Example 1:

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:

# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.

# Example 3:

# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0

 

# Constraints:

#     1 <= nums.length <= 104
#     -1000 <= nums[i] <= 1000

 

# Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.3M
# Submissions
# 2.2M
# Acceptance Rate
# 59.9%
# Topics
# Array
# Prefix Sum
# Companies
# Hint 1
# Create an array sumLeft where sumLeft[i] is the sum of all the numbers to the left of index i.
# Hint 2
# Create an array sumRight where sumRight[i] is the sum of all the numbers to the right of index i.
# Hint 3
# For each index i, check if sumLeft[i] equals sumRight[i]. If so, return i. If no such i is found, return -1.


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        # for i, num in enumerate(nums):
        #     if left_sum * 2 == total_sum - num: Could also use this but it's much slower due to multiplication in the if statement
        #         return i
        #     left_sum += num
        
        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1    

print(Solution.pivotIndex(Solution, [1,7,3,6,5,6]))
print(Solution.pivotIndex(Solution, [1,2,3]))
print(Solution.pivotIndex(Solution, [2,1,-1]))
print(Solution.pivotIndex(Solution, [-1,-1,-1,1,1,1]))

# extremely slow bottom 5 percent solution
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        temp = nums.copy()
        temp = [0] + temp
        n = len(nums)
        nums = nums + [0]
        for i in range(1, n+1):
            temp[i] = temp[i] + temp[i-1]
        for i in range(n-1, -1, -1):
            nums[i] = nums[i] + nums[i+1]
        nums.pop()
        temp.remove(0)
        for i in range(0, n):
            for j in range(i, n):
                if temp[i] == nums[i]:
                    return i
        print(temp)
        print(nums)
        return -1
