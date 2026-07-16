# LeetCode 0827 - Making A Large Island
# https://leetcode.com/problems/making-a-large-island/

class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        sizes = {0: 0}
        island_id = 2

        def dfs(r: int, c: int, iid: int) -> int:
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = iid
            return 1 + dfs(r + 1, c, iid) + dfs(r - 1, c, iid) + dfs(r, c + 1, iid) + dfs(r, c - 1, iid)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    sizes[island_id] = dfs(i, j, island_id)
                    island_id += 1

        ans = max(sizes.values()) if sizes else 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                seen = set()
                total = 1
                for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= ni < n and 0 <= nj < n:
                        iid = grid[ni][nj]
                        if iid > 1 and iid not in seen:
                            seen.add(iid)
                            total += sizes[iid]
                ans = max(ans, total)
        return ans
