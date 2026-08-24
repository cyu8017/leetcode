# LeetCode 3449 - Maximize the Minimum Game Score
# https://leetcode.com/problems/maximize-the-minimum-game-score/

from typing import List


class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def ok(mid: int) -> bool:
            need = extra = 0
            for p in points:
                req = (mid + p - 1) // p
                if req > extra:
                    visits = req - extra
                    need += 2 * visits - 1
                    extra = visits - 1
                else:
                    need += 1
                    extra = 0
                if need > m:
                    return False
            return need <= m

        lo, hi = 0, 10**18
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
