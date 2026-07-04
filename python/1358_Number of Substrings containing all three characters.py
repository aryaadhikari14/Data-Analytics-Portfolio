# Leetcode 1358: Number of substring contaning all three characters
# Difficulty : Medium
# Language : Python

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #Track the last seen index of 'a', 'b', and 'c'
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        for i, char in enumerate(s):
            # Update the position of the current character
            last_seen[char] = i
            # The number of valid substrings ending at index i is determined
            # by the minimum index among the last seen positions of 'a', 'b', and 'c'.
            # if any character hasn't been seen yet, min() will return -1, adding 0 to count.
            count += min(last_seen['a'], last_seen['b'], last_seen['c']) + 1
        return count    
