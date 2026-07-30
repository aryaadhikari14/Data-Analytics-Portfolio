# Leetcode 3014: Minimum number of pushes to type word I
# Difficulty : Easy
# Language : Python

class Solution:
    def minimumPushes(self, word: str) -> int:
       n = len(word)
       ans = 0

       for i in range(n):
           ans += i // 8 + 1
       return ans
