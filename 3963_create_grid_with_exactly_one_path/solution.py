# LeetCode 3963 - Create Grid With Exactly One Path
# https://leetcode.com/problems/create-grid-with-exactly-one-path/

from typing import List


class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        g = []
        for i in range(m):
            row = ["#"] * n
            if i == 0:
                for j in range(n):
                    row[j] = "."
            row[n - 1] = "."
            g.append("".join(row))
        return g
