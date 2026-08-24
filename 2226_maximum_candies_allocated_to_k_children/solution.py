# LeetCode 2226 - Maximum Candies Allocated to K Children
# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        lo, hi = 0, max(candies) if candies else 0

        def can(mid: int) -> bool:
            if mid == 0:
                return True
            cnt = 0
            for c in candies:
                cnt += c // mid
                if cnt >= k:
                    return True
            return False

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
