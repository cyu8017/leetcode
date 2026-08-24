# LeetCode 2616 - Minimize the Maximum Difference of Pairs
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]

        def ok(d: int) -> bool:
            cnt = 0
            i = 0
            while i + 1 < len(nums):
                if nums[i + 1] - nums[i] <= d:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p

        while lo < hi:
            mid = (lo + hi) >> 1
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
