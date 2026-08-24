# LeetCode 2137 - Pour Water Between Buckets to Make Water Levels Equal
# https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

from typing import List
class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> int:
        lo = 0
        hi = 0
        for b in buckets:
            hi = max(hi, b)
        for iter in range(60):
            mid = (lo + hi) / 2
            have = 0
            need = 0
            for b in buckets:
                if b >= mid:
                    have += b - mid
                else:
                    need += mid - b
            if have * (1 - loss / 100) >= need:
                lo = mid
            else:
                hi = mid
        return lo
