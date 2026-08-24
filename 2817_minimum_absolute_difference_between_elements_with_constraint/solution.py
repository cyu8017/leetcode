# LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
# https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

from typing import List


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0:
            ans0 = 10**18
            for i in range(1, len(nums)):
                ans0 = min(ans0, abs(nums[i] - nums[i - 1]))
            return ans0
        ans = 10**18
        arr = []

        def insert(v: int) -> None:
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) >> 1
                if arr[mid] < v:
                    lo = mid + 1
                else:
                    hi = mid
            arr.insert(lo, v)

        def lower_bound(v: int) -> int:
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) >> 1
                if arr[mid] < v:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        for i in range(x, len(nums)):
            insert(nums[i - x])
            cur = nums[i]
            idx = lower_bound(cur)
            if idx < len(arr):
                ans = min(ans, arr[idx] - cur)
            if idx > 0:
                ans = min(ans, cur - arr[idx - 1])
        return ans
