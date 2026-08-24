# LeetCode 2606 - Find the Substring With Maximum Cost
# https://leetcode.com/problems/find-the-substring-with-maximum-cost/

from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        val = [i + 1 for i in range(26)]
        for i, ch in enumerate(chars):
            val[ord(ch) - 97] = vals[i]
        best = 0
        cur = 0
        for c in s:
            cur += val[ord(c) - 97]
            if cur < 0:
                cur = 0
            if cur > best:
                best = cur
        return best
