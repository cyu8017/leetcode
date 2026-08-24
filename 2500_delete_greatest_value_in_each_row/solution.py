# LeetCode 2500 - Delete Greatest Value in Each Row
# https://leetcode.com/problems/delete-greatest-value-in-each-row/

from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        ans = 0
        n = len(grid[0])
        for c in range(n):
            mx = 0
            for row in grid:
                if row[c] > mx:
                    mx = row[c]
            ans += mx
        return ans
