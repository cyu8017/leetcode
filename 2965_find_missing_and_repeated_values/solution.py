# LeetCode 2965 - Find Missing and Repeated Values
# https://leetcode.com/problems/find-missing-and-repeated-values/

from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = [0] * (n * n + 1)
        for i in range(n):
            for j in range(n):
                freq[grid[i][j]] += 1
        rep = 0
        miss = 0
        for i in range(1, n * n + 1):
            if freq[i] == 2:
                rep = i
            if freq[i] == 0:
                miss = i
        return [rep, miss]
