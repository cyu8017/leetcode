# LeetCode 3359 - Find Sorted Submatrices With Maximum Element at Most K
# https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/

from typing import List


class Solution:
    def countSortedMatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for r1 in range(m):
            for r2 in range(r1, m):
                for c1 in range(n):
                    for c2 in range(c1, n):
                        good = True
                        i = r1
                        while i <= r2 and good:
                            for j in range(c1, c2 + 1):
                                if grid[i][j] > k:
                                    good = False
                                    break
                                if j > c1 and grid[i][j] < grid[i][j - 1]:
                                    good = False
                                    break
                                if i > r1 and grid[i][j] < grid[i - 1][j]:
                                    good = False
                                    break
                            i += 1
                        if good:
                            ans += 1
        return ans
