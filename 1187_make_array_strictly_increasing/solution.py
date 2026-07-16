# LeetCode 1187 - Make Array Strictly Increasing
# https://leetcode.com/problems/make-array-strictly-increasing/

import bisect


class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2 = sorted(set(arr2))
        dp = {-1: 0}
        for num in arr1:
            new_dp: dict[int, int] = {}
            for prev, ops in dp.items():
                if num > prev:
                    new_dp[num] = min(new_dp.get(num, float("inf")), ops)
                idx = bisect.bisect_right(arr2, prev)
                if idx < len(arr2):
                    chosen = arr2[idx]
                    new_dp[chosen] = min(new_dp.get(chosen, float("inf")), ops + 1)
            dp = new_dp
            if not dp:
                return -1
        return min(dp.values())
