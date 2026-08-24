# LeetCode 3838 - Weighted Word Mapping
# https://leetcode.com/problems/weighted-word-mapping/

from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for w in words:
            s = 0
            for c in w:
                s = (s + weights[ord(c) - 97]) % 26
            ans.append(chr(97 + (25 - s)))
        return "".join(ans)
