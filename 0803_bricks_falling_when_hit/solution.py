# LeetCode 0803 - Bricks Falling When Hit
# https://leetcode.com/problems/bricks-falling-when-hit/

from typing import List


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        roof = m * n
        parent = list(range(roof + 1))
        size = [1] * (roof + 1)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            parent[ra] = rb
            size[rb] += size[ra]

        def idx(r: int, c: int) -> int:
            return r * n + c

        def neighbors(r: int, c: int):
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < m and 0 <= nc < n:
                    yield nr, nc

        status = [row[:] for row in grid]
        for r, c in hits:
            status[r][c] = 0

        for r in range(m):
            for c in range(n):
                if status[r][c] == 0:
                    continue
                if r == 0:
                    union(idx(r, c), roof)
                for nr, nc in neighbors(r, c):
                    if status[nr][nc] == 1:
                        union(idx(r, c), idx(nr, nc))

        answer = [0] * len(hits)
        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]
            if grid[r][c] == 0:
                continue
            prev = size[find(roof)]
            status[r][c] = 1
            if r == 0:
                union(idx(r, c), roof)
            for nr, nc in neighbors(r, c):
                if status[nr][nc] == 1:
                    union(idx(r, c), idx(nr, nc))
            curr = size[find(roof)]
            answer[i] = max(0, curr - prev - 1)
        return answer
