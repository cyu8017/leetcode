# LeetCode 3548 - Equal Sum Grid Partition II
# https://leetcode.com/problems/equal-sum-grid-partition-ii/

from typing import List


def rotate3548(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    t = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            t[j][i] = grid[i][j]
    return t


def check3548(g: List[List[int]]) -> bool:
    m, n = len(g), len(g[0])
    s1 = s2 = 0
    cnt1 = {}
    cnt2 = {}
    for row in g:
        for x in row:
            s2 += x
            cnt2[x] = cnt2.get(x, 0) + 1
    for i in range(m - 1):
        for x in g[i]:
            s1 += x
            s2 -= x
            cnt1[x] = cnt1.get(x, 0) + 1
            cnt2[x] = cnt2.get(x, 0) - 1
        if s1 == s2:
            return True
        if s1 < s2:
            diff = s2 - s1
            if cnt2.get(diff, 0) > 0:
                if (
                    (m - i - 1 > 1 and n > 1)
                    or (i == m - 2 and (g[i + 1][0] == diff or g[i + 1][n - 1] == diff))
                    or (n == 1 and (g[i + 1][0] == diff or g[m - 1][0] == diff))
                ):
                    return True
        else:
            diff = s1 - s2
            if cnt1.get(diff, 0) > 0:
                if (
                    (i + 1 > 1 and n > 1)
                    or (i == 0 and (g[0][0] == diff or g[0][n - 1] == diff))
                    or (n == 1 and (g[0][0] == diff or g[i][0] == diff))
                ):
                    return True
    return False


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        return check3548(grid) or check3548(rotate3548(grid))
