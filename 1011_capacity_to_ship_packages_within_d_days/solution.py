# LeetCode 1011 - Capacity To Ship Packages Within D Days
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)

        def can(cap: int) -> bool:
            need = cur = 1
            for w in weights:
                if cur + w > cap:
                    need += 1
                    cur = 0
                cur += w
            return need <= days

        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
