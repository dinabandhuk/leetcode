# 345. Reverse Vowels of a String
# Easy
# Topics
# Companies

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

#     1 <= s.length <= 3 * 105
#     s consist of printable ASCII characters.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        strlist = list(s)
        left, right = 0, len(strlist) -1
        
        while left<right:
            if strlist[left] not in vowels:
                left +=1
            elif strlist[right] not in vowels:
                right -=1
            else:
                strlist[left], strlist[right] = strlist[right], strlist[left]
                left += 1
                right -= 1
        return "".join(strlist)

print(Solution.reverseVowels(Solution, "IceCreAm"))
                
                