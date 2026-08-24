# LeetCode 2560 - House Robber IV
# https://leetcode.com/problems/house-robber-iv/

from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        lo, hi = min(nums), max(nums)

        def ok(cap: int) -> bool:
            cnt = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= k

        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
