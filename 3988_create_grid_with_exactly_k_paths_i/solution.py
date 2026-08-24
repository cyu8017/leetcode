# LeetCode 3988 - Create Grid With Exactly K Paths I
# https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

from typing import List


class Solution:
    def createGrid(self, m: int, n: int, k: int) -> List[str]:
        cands = []
        if k == 1:
            cands.append(["."])
        elif k == 2:
            cands.append(["..", ".."])
        elif k == 3:
            cands.append(["..", "..", ".."])
            cands.append(["...", "..."])
        elif k == 4:
            cands.append(["..", "..", "..", ".."])
            cands.append(["....", "...."])
            cands.append(["..#", "...", "#.."])
        for pat in cands:
            pr = len(pat)
            pc = len(pat[0])
            if pr > m or pc > n:
                continue
            result = ["#" * n for _ in range(m)]
            for i in range(pr):
                row = list(result[i])
                for j in range(pc):
                    row[j] = pat[i][j]
                result[i] = "".join(row)
            for i in range(pr, m):
                row = list(result[i])
                row[pc - 1] = "."
                result[i] = "".join(row)
            for j in range(pc, n):
                row = list(result[m - 1])
                row[j] = "."
                result[m - 1] = "".join(row)
            return result
        return []
