# LeetCode 0524 - Longest Word in Dictionary through Deleting
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        def is_subsequence(word: str) -> bool:
            index = 0
            for char in s:
                if index < len(word) and word[index] == char:
                    index += 1
            return index == len(word)

        best = ""
        for word in dictionary:
            if is_subsequence(word) and (len(word) > len(best) or (len(word) == len(best) and word < best)):
                best = word
        return best
