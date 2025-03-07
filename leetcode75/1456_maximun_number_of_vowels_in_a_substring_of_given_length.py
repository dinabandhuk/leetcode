# 1456. Maximum Number of Vowels in a Substring of Given Length
# Medium
# Topics
# Companies
# Hint

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

 

# Constraints:

#     1 <= s.length <= 10^5
#     s consists of lowercase English letters.
#     1 <= k <= s.length

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 483K
# Submissions
# 807.1K
# Acceptance Rate
# 59.8%
# Topics
# String
# Sliding Window

# this beats 96.4 % of participants with 47ms runtime. 107 tests
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = current_vowels = sum(1 for i in range(k) if s[i] in vowels)
        
        for i in range(k, len(s)):
            current_vowels += (s[i] in vowels) - (s[i-k] in vowels)
            if max_vowels < current_vowels: # don't use max(max_vowels, current_vowels) because it's slower due to hindering branch prediction in CPU
                max_vowels = current_vowels
        return max_vowels






print(Solution.maxVowels(Solution, "abciiidef", 3))

# infficient K*N runtime
class Solution:
    @staticmethod
    def count_vowels(somelist):
        counter =0
        small_vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(0, len(somelist)):
            for j in range(0, len(small_vowels)):
                if somelist [i] == small_vowels[j]:
                    counter += 1
        return counter

    def maxVowels(self, s: str, k: int) -> int:
        string = list(s)
        max_vowels = 0
        for i in range(0, len(string)-k):
            num_vowels = self.count_vowels(string[i:i+k])
            if num_vowels > max_vowels :
                max_vowels = num_vowels
        return max_vowels