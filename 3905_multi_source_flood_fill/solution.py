# LeetCode 3905 - Multi Source Flood Fill
# https://leetcode.com/problems/multi-source-flood-fill/

from typing import Dict, List


class Solution:
    def colorGrid(self, n: int, m: int, sources: List[List[int]]) -> List[List[int]]:
        ans = [[0] * m for _ in range(n)]
        q = [s[:] for s in sources]
        dirs = [-1, 0, 1, 0, -1]
        for s in q:
            ans[s[0]][s[1]] = s[2]
        while q:
            vis: Dict[int, int] = {}
            for curr in q:
                r, c, color = curr[0], curr[1], curr[2]
                for i in range(4):
                    x = r + dirs[i]
                    y = c + dirs[i + 1]
                    if 0 <= x < n and 0 <= y < m and ans[x][y] == 0:
                        key = (x << 32) | (y & 0xFFFFFFFF)
                        if key not in vis or color > vis[key]:
                            vis[key] = color
            q = []
            for key, color in vis.items():
                x = key >> 32
                y = key & 0xFFFFFFFF
                ans[x][y] = color
                q.append([x, y, color])
        return ans
