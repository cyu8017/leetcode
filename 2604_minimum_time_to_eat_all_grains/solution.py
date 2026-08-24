# LeetCode 2604 - Minimum Time to Eat All Grains
# https://leetcode.com/problems/minimum-time-to-eat-all-grains/

from typing import List


class Solution:
    def minimumTime(self, hens: List[int], grains: List[int]) -> int:
        hens.sort()
        grains.sort()

        def ok(t: int) -> bool:
            j = 0
            for h in hens:
                if j >= len(grains):
                    return True
                if grains[j] >= h:
                    while j < len(grains) and grains[j] - h <= t:
                        j += 1
                else:
                    if h - grains[j] > t:
                        return False
                    left = h - grains[j]
                    max_right1 = t - 2 * left
                    max_right2 = (t - left) // 2
                    reach = h
                    if max_right1 > max_right2:
                        if max_right1 > 0:
                            reach = h + max_right1
                    else:
                        if max_right2 > 0:
                            reach = h + max_right2
                    while j < len(grains) and grains[j] <= reach:
                        j += 1
            return j >= len(grains)

        lo, hi = 0, 2000000000
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
