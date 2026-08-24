# LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
# https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

from typing import List


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cnt1 = [0, 0, 0]
        cnt2 = [0, 0, 0]
        for i in range(n):
            for j in range(n):
                x = grid[i][j]
                a = i == j and i <= n // 2
                b = i + j == n - 1 and i <= n // 2
                c = j == n // 2 and i >= n // 2
                if a or b or c:
                    cnt1[x] += 1
                else:
                    cnt2[x] += 1
        ans = n * n
        for i in range(3):
            for j in range(3):
                if i != j:
                    ans = min(ans, n * n - cnt1[i] - cnt2[j])
        return ans
