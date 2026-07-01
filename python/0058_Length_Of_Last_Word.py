# Leetcode 58 : Length of last word
# Difficulty : Easy 
# Language : Python

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                break
            count += 1
        return count
