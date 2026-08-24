# LeetCode 3073 - Maximum Increasing Triplet Value
# https://leetcode.com/problems/maximum-increasing-triplet-value/

from typing import List, Optional


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(nums[i], right[i + 1])
        ts = []

        def add(x: int) -> None:
            lo = 0
            hi = len(ts)
            while lo < hi:
                mid = (lo + hi) >> 1
                if ts[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == len(ts) or ts[lo] != x:
                ts.insert(lo, x)

        def lower(x: int) -> Optional[int]:
            lo = 0
            hi = len(ts)
            while lo < hi:
                mid = (lo + hi) >> 1
                if ts[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return ts[lo - 1] if lo > 0 else None

        add(nums[0])
        ans = 0
        for j in range(1, n - 1):
            if right[j + 1] > nums[j]:
                it = lower(nums[j])
                if it is not None:
                    ans = max(ans, it - nums[j] + right[j + 1])
            add(nums[j])
        return ans
