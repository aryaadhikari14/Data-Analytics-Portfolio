# Leetcode 0012: Integer to Roman
# Difficulty : Medium
# Language : Python

class Solution:
    def intToRoman(self, num: int) -> str:
        # map values to roman symbols in descending order
        roman_mapping = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ] 
        result = []
        # Loop through the map from largest value to smallest
        for value, symbol in roman_mapping:
            # if num is 0, we can stop early
            if num == 0:
                break
            # determine how many times this symbol fits into the number 
            count = num // value
            if count > 0:
                result.append(symbol * count)
                # reduce num by the amount we just converted
                num %= value
        # join the list into a single string
        return "".join(result)    
