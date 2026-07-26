# Leetcode 628: Maximum products of three numbers
# Difficulty : Easy
# Language : Python

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        return max(
            nums[-1] *
nums[-2] * nums[-3],
            nums[0] * nums[1]
* nums[-1]
        )
