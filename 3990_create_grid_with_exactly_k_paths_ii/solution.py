# LeetCode 3990 - Create Grid With Exactly K Paths II
# https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

from typing import List


class Solution:
    def BitWidth(self, k: int) -> int:
        w = 0
        while k != 0:
            w += 1
            k >>= 1
        return w

    def createGrid(self, k: int) -> List[str]:
        if k <= 0:
            return []
        l = self.BitWidth(k)
        m = 2 * l
        n = l + 3
        result = [["#"] * n for _ in range(m)]
        for i in range(l):
            r = 2 * i
            result[r][i] = result[r][i + 1] = result[r + 1][i] = result[r + 1][i + 1] = "."
            if (k & (1 << i)) != 0:
                for c in range(i + 2, n):
                    result[r][c] = "."
        for r in range(m):
            result[r][n - 1] = "."
        return ["".join(row) for row in result]
