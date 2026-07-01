# Leetcode 60: Permutation Sequence
# Difficulty : Hard
# Language : Python

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
           # create a list of numbersfrom 1 to n
           numbers = [str(i) for i in range(1, n + 1)]
           #precompute factorials up to n-1
           factorials = [1] * n
           for i in range(1, n):
            factorials[i] = factorials[i - 1] * i
           # convert k to 0-indexed to match list indexing 
           k -= 1
           result = []
           # determine each digit of the permutation
           for i in range(n - 1, -1, -1):
            #calculate the index of the next number to pick
            index = k // factorials[i]
            result.append(numbers.pop(index))
            #update k for the next iteration
            k %= factorials[i]
           return "".join(result)
