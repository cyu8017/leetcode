# LeetCode 0576 - Out of Boundary Paths
# https://leetcode.com/problems/out-of-boundary-paths/


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        mod = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        result = 0
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        for _ in range(maxMove):
            nxt = [[0] * n for _ in range(m)]
            for row in range(m):
                for col in range(n):
                    ways = dp[row][col]
                    if ways == 0:
                        continue
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            nxt[nr][nc] = (nxt[nr][nc] + ways) % mod
                        else:
                            result = (result + ways) % mod
            dp = nxt

        return result
