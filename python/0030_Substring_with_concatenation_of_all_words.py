# Leetcode 30: Substring with Concatention of all words
# Difficulty : Hard
# Language : Python

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
             return []
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_counts = Counter(words)
        result_indices = []
        # we only need to check starting positions where a full substring can fit
        for i in range(len(s) - total_len + 1):
            # take the current substring slice of length total_len
            sub_str = s[i:i + total_len]
            # break the slice down into individual word chunks
            seen_words = []
            for j in range(0, total_len, word_len):
                seen_words.append(sub_str[j:j + word_len])
            # compare the frequencies of chunks to our target counts
            if Counter(seen_words) == word_counts:
                result_indices.append(i)
        return result_indices
