# 443. String Compression
# Medium
# Topics
# Companies
# Hint

# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

#     If the group's length is 1, append the character to s.
#     Otherwise, append the character followed by the group's length.

# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

 

# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

# Example 2:

# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.

# Example 3:

# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

 

# Constraints:

#     1 <= chars.length <= 2000
#     chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 796.9K
# Submissions
# 1.4M
# Acceptance Rate
# 57.3%
# Topics
# Two Pointers
# String
# Companies
# Hint 1
# How do you know if you are at the end of a consecutive group of characters?

class Solution:
    def compress(self, chars: list[str]) -> int:
        read, write = 0, 0
        n = len(chars)
        while read < n:
            current_char = chars[read]
            count = 0
            
            while read < n and chars[read] == current_char:
                read += 1
                count +=1
            chars[write] = current_char
            write += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write

print(Solution.compress(Solution, ["a","a","b","b","c","c","c"]))
print(Solution.compress(Solution, ["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

# https://leetcode.com/problems/string-compression/solutions/6492410/optimized-character-compression-the-fastest-solution-i-ve-found

class Solution:
    def compress(self, chars: list[str]) -> int:
        compressed = [chars[0]]
        char_count = 0
        current_char = chars[0]
        for char in chars:
            if char == current_char:
                char_count += 1
            else:
                if char_count != 1:
                    compressed.extend(str(char_count))
                compressed.append(char)
                current_char = char
                char_count = 1
        if char_count != 1:
            compressed.extend(str(char_count))
        chars.clear()
        chars.extend(compressed)
        return len(compressed)
                
        
