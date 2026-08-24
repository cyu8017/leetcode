# LeetCode 2251 - Number of Flowers in Full Bloom
# https://leetcode.com/problems/number-of-flowers-in-full-bloom/

from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = [f[0] for f in flowers]
        end = [f[1] for f in flowers]
        start.sort()
        end.sort()

        def upper_bound(a: List[int], t: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) >> 1
                if a[mid] <= t:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def lower_bound(a: List[int], t: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) >> 1
                if a[mid] < t:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        return [upper_bound(start, t) - lower_bound(end, t) for t in people]
