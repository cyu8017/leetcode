# LeetCode 2788 - Split Strings by Separator
# https://leetcode.com/problems/split-strings-by-separator/

from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for w in words:
            start = 0
            for i in range(len(w) + 1):
                if i == len(w) or w[i] == separator:
                    if i > start:
                        ans.append(w[start:i])
                    start = i + 1
        return ans
