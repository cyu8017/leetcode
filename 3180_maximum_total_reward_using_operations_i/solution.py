# LeetCode 3180 - Maximum Total Reward Using Operations I
# https://leetcode.com/problems/maximum-total-reward-using-operations-i/

from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        n = len(rewardValues)
        f = [-1] * (rewardValues[n - 1] << 1)

        def upper_bound(a: List[int], x: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) >> 1
                if a[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def dfs(x: int) -> int:
            if f[x] != -1:
                return f[x]
            idx = upper_bound(rewardValues, x)
            f[x] = 0
            for it in range(idx, n):
                f[x] = max(f[x], rewardValues[it] + dfs(x + rewardValues[it]))
            return f[x]

        return dfs(0)
