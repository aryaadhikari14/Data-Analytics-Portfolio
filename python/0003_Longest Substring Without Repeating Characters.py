# Leetcode 0003: Longest substring without repeating characters
# Difficulty : Medium
# Language : Python

Class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
     # Hash table to store the last seen index of each character
     char_map = {}
     left = 0
     max_length = 0
     for right in range(len(s)):
        current_char = s[right]
        #if the character is already in our map and within our current window
        if current_char in char_map and char_map[current_char] >= left:
            # move the left pointer past previous occurrence
            left = char_map[current_char] + 1
        #update/insert the character's newest position
        char_map[current_char] = right
        # calculate the current window size and update max_length
        current_window_len = right - left + 1
        max_length = max(max_length, current_window_len)
     return max_length    
