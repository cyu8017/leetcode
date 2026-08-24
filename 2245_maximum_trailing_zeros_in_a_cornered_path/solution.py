# LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
# https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

from typing import List, Tuple


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def fact(x: int) -> Tuple[int, int]:
            t = f = 0
            while x % 2 == 0:
                t += 1
                x //= 2
            while x % 5 == 0:
                f += 1
                x //= 5
            return t, f

        m, n = len(grid), len(grid[0])
        left2 = [[0] * n for _ in range(m)]
        left5 = [[0] * n for _ in range(m)]
        up2 = [[0] * n for _ in range(m)]
        up5 = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                p0, p1 = fact(grid[i][j])
                left2[i][j] = up2[i][j] = p0
                left5[i][j] = up5[i][j] = p1
                if j > 0:
                    left2[i][j] += left2[i][j - 1]
                    left5[i][j] += left5[i][j - 1]
                if i > 0:
                    up2[i][j] += up2[i - 1][j]
                    up5[i][j] += up5[i - 1][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                cell = fact(grid[i][j])
                L2, L5 = left2[i][j], left5[i][j]
                R2 = left2[i][n - 1] - left2[i][j] + cell[0]
                R5 = left5[i][n - 1] - left5[i][j] + cell[1]
                U2, U5 = up2[i][j], up5[i][j]
                D2 = up2[m - 1][j] - up2[i][j] + cell[0]
                D5 = up5[m - 1][j] - up5[i][j] + cell[1]
                cands = [
                    (L2 + U2 - cell[0], L5 + U5 - cell[1]),
                    (L2 + D2 - cell[0], L5 + D5 - cell[1]),
                    (R2 + U2 - cell[0], R5 + U5 - cell[1]),
                    (R2 + D2 - cell[0], R5 + D5 - cell[1]),
                ]
                for a, b in cands:
                    ans = max(ans, min(a, b))
        return ans
