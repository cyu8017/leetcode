# LeetCode 2145 - Count the Hidden Sequences
# https://leetcode.com/problems/count-the-hidden-sequences/

from typing import List
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        cur = 0
        mn = 0
        mx = 0
        for d in differences:
            cur += d
            mn = min(mn, cur)
            mx = max(mx, cur)
        res = (upper - lower) - (mx - mn) + 1
        return 0 if res < 0 else res
