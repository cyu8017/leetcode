from collections import deque
from typing import List

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = sum(mat[r][c] << (r * n + c) for r in range(m) for c in range(n))
        masks = []
        for r in range(m):
            for c in range(n):
                mask = 0
                for dr, dc in ((0,0),(1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        mask ^= 1 << (nr * n + nc)
                masks.append(mask)
        queue, seen = deque([(start, 0)]), {start}
        while queue:
            state, distance = queue.popleft()
            if state == 0: return distance
            for mask in masks:
                nxt = state ^ mask
                if nxt not in seen:
                    seen.add(nxt); queue.append((nxt, distance + 1))
        return -1
