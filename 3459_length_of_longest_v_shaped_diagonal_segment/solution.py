# LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        next_dir = [1, 2, 3, 0]
        memo = {}

        def key(i: int, j: int, d: int, turned: int, expect: int) -> int:
            return ((((i * 101 + j) * 5 + d) * 3 + turned) * 5 + expect)

        def dfs(i: int, j: int, d: int, turned: int, expect: int) -> int:
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != expect:
                return 0
            k = key(i, j, d, turned, expect)
            if k in memo:
                return memo[k]
            ni, nj = i + dirs[d][0], j + dirs[d][1]
            nx = 0 if expect == 2 else 2
            best = 1 + dfs(ni, nj, d, turned, nx)
            if turned == 0:
                nd = next_dir[d]
                ti, tj = i + dirs[nd][0], j + dirs[nd][1]
                cand = 1 + dfs(ti, tj, nd, 1, nx)
                if cand > best:
                    best = cand
            memo[k] = best
            return best

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                for d in range(4):
                    ni, nj = i + dirs[d][0], j + dirs[d][1]
                    best = 1 + dfs(ni, nj, d, 0, 2)
                    if best > ans:
                        ans = best
                if ans < 1:
                    ans = 1
        return ans
