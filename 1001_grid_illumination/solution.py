# LeetCode 1001 - Grid Illumination
# https://leetcode.com/problems/grid-illumination/

from collections import defaultdict


class Solution:
    def gridIllumination(
        self, n: int, lamps: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        rows: dict[int, int] = defaultdict(int)
        cols: dict[int, int] = defaultdict(int)
        diag1: dict[int, int] = defaultdict(int)
        diag2: dict[int, int] = defaultdict(int)
        lit = set()
        for r, c in lamps:
            if (r, c) in lit:
                continue
            lit.add((r, c))
            rows[r] += 1
            cols[c] += 1
            diag1[r - c] += 1
            diag2[r + c] += 1

        ans = []
        for r, c in queries:
            ans.append(1 if rows[r] or cols[c] or diag1[r - c] or diag2[r + c] else 0)
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i, j) in lit:
                        lit.remove((i, j))
                        rows[i] -= 1
                        cols[j] -= 1
                        diag1[i - j] -= 1
                        diag2[i + j] -= 1
        return ans
