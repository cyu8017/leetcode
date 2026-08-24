# LeetCode 2416 - Sum of Prefix Scores of Strings
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = {"child": [None] * 26, "cnt": 0}
        for w in words:
            cur = root
            for ch in w:
                c = ord(ch) - 97
                if cur["child"][c] is None:
                    cur["child"][c] = {"child": [None] * 26, "cnt": 0}
                cur = cur["child"][c]
                cur["cnt"] += 1
        ans = [0] * len(words)
        for i, w in enumerate(words):
            cur = root
            s = 0
            for ch in w:
                cur = cur["child"][ord(ch) - 97]
                s += cur["cnt"]
            ans[i] = s
        return ans
