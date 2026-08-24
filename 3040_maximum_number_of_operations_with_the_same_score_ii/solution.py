# LeetCode 3040 - Maximum Number of Operations With the Same Score II
# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        f = []
        s = 0

        def dfs(i: int, j: int) -> int:
            if j - i < 1:
                return 0
            if f[i][j] != -1:
                return f[i][j]
            ans = 0
            if nums[i] + nums[i + 1] == s:
                ans = max(ans, 1 + dfs(i + 2, j))
            if nums[i] + nums[j] == s:
                ans = max(ans, 1 + dfs(i + 1, j - 1))
            if nums[j - 1] + nums[j] == s:
                ans = max(ans, 1 + dfs(i, j - 2))
            f[i][j] = ans
            return ans

        def g(i0: int, j0: int, score: int) -> int:
            nonlocal f, s
            f = [[-1] * n for _ in range(n)]
            s = score
            return dfs(i0, j0)

        a = g(2, n - 1, nums[0] + nums[1])
        b = g(0, n - 3, nums[n - 1] + nums[n - 2])
        c = g(1, n - 2, nums[0] + nums[n - 1])
        return 1 + max(a, max(b, c))
