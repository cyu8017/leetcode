# LeetCode 3891 - Minimum Increase To Maximize Special Indices
# https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

from typing import List


class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[-1, -1] for _ in range(n)]

        def dfs(i: int, j: int) -> int:
            if i >= n - 1:
                return 0
            if f[i][j] != -1:
                return f[i][j]
            cost = max(0, max(nums[i - 1], nums[i + 1]) + 1 - nums[i])
            ans = cost + dfs(i + 2, j)
            if j > 0:
                ans = min(ans, dfs(i + 1, 0))
            f[i][j] = ans
            return ans

        return dfs(1, (n & 1) ^ 1)
