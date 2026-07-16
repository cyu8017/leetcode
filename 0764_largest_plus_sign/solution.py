# LeetCode 0764 - Largest Plus Sign
# https://leetcode.com/problems/largest-plus-sign/

from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        banned = {r * n + c for r, c in mines}
        arms = [[0] * n for _ in range(n)]
        best = 0

        for r in range(n):
            count = 0
            for c in range(n):
                count = 0 if r * n + c in banned else count + 1
                arms[r][c] = count
            count = 0
            for c in range(n - 1, -1, -1):
                count = 0 if r * n + c in banned else count + 1
                arms[r][c] = min(arms[r][c], count)

        for c in range(n):
            count = 0
            for r in range(n):
                count = 0 if r * n + c in banned else count + 1
                arms[r][c] = min(arms[r][c], count)
            count = 0
            for r in range(n - 1, -1, -1):
                count = 0 if r * n + c in banned else count + 1
                arms[r][c] = min(arms[r][c], count)
                best = max(best, arms[r][c])

        return best
