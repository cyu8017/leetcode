# LeetCode 3634 - Minimum Removals to Balance Array
# https://leetcode.com/problems/minimum-removals-to-balance-array/

from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def lower_bound(a: List[int], target: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) >> 1
                if a[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        cnt = 0
        for i in range(n):
            j = n
            if nums[i] * k <= nums[n - 1]:
                target = nums[i] * k + 1
                j = lower_bound(nums, target)
            cnt = max(cnt, j - i)
        return n - cnt
