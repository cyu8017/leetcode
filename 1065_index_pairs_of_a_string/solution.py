# LeetCode 1065 - Index Pairs of a String
# https://leetcode.com/problems/index-pairs-of-a-string/

class Solution:
    def indexPairs(self, text: str, words: list[str]) -> list[list[int]]:
        word_set = set(words)
        ans: list[list[int]] = []
        n = len(text)
        for i in range(n):
            for j in range(i, n):
                if text[i : j + 1] in word_set:
                    ans.append([i, j])
        return ans
