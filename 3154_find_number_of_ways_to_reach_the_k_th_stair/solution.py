# LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
# https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/


class Solution:
    def waysToReachStair(self, k: int) -> int:
        f = {}

        def dfs(i: int, j: int, jump: int) -> int:
            if i > k + 1:
                return 0
            key = (i, j, jump)
            if key in f:
                return f[key]
            ans = 0
            if i == k:
                ans += 1
            if i > 0 and j == 0:
                ans += dfs(i - 1, 1, jump)
            ans += dfs(i + (2 ** jump), 0, jump + 1)
            f[key] = ans
            return ans

        return dfs(1, 0, 0)
