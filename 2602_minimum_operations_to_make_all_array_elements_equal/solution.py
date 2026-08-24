# LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
# https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        def lower_bound(x: int) -> int:
            lo, hi = 0, n
            while lo < hi:
                mid = (lo + hi) >> 1
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        ans = [0] * len(queries)
        for qi, q in enumerate(queries):
            i = lower_bound(q)
            left = q * i - pref[i]
            right = pref[n] - pref[i] - q * (n - i)
            ans[qi] = left + right
        return ans
