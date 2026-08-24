# LeetCode 3129 - Find All Possible Stable Binary Arrays I
# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1000000007
        f = [[[-1, -1] for _ in range(one + 1)] for _ in range(zero + 1)]

        def dfs(i: int, j: int, k: int) -> int:
            if i < 0 or j < 0:
                return 0
            if i == 0:
                return 1 if k == 1 and j <= limit else 0
            if j == 0:
                return 1 if k == 0 and i <= limit else 0
            if f[i][j][k] != -1:
                return f[i][j][k]
            if k == 0:
                res = (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - dfs(i - limit - 1, j, 1) + MOD) % MOD
            else:
                res = (dfs(i, j - 1, 0) + dfs(i, j - 1, 1) - dfs(i, j - limit - 1, 0) + MOD) % MOD
            f[i][j][k] = res
            return res

        return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD
