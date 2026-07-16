# LeetCode 1078 - Occurrences After Bigram
# https://leetcode.com/problems/occurrences-after-bigram/

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        words = text.split()
        return [
            words[i + 2]
            for i in range(len(words) - 2)
            if words[i] == first and words[i + 1] == second
        ]
