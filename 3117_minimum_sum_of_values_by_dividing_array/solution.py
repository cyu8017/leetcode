# LeetCode 3117 - Minimum Sum of Values by Dividing Array
# https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

from typing import List


class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        INF = 1 << 29
        n = len(nums)
        m = len(andValues)
        f = {}

        def dfs(i: int, j: int, a: int) -> int:
            if n - i < m - j:
                return INF
            if j == m:
                return 0 if i == n else INF
            a &= nums[i]
            if a < andValues[j]:
                return INF
            key = (i, j, a)
            if key in f:
                return f[key]
            ans = dfs(i + 1, j, a)
            if a == andValues[j]:
                ans = min(ans, dfs(i + 1, j + 1, -1) + nums[i])
            f[key] = ans
            return ans

        ans = dfs(0, 0, -1)
        return ans if ans < INF else -1
