# LeetCode 3281 - Maximize Score of Numbers in Ranges
# https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

from typing import List


class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        n = len(start)

        def ok(mid: int) -> bool:
            prev = start[0]
            for i in range(1, len(start)):
                need = prev + mid
                cur = start[i]
                if need > cur + d:
                    return False
                prev = need if need > cur else cur
            return True

        lo, hi = 0, start[n - 1] + d - start[0] + 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
