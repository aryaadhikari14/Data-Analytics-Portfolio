# Leetcode 342: Power of four
# Difficulty : Easy
# Language : Python

Class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1
