# Leetcode 231: Power of two
# Difficulty : Easy
# Language : Python

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
