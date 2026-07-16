# LeetCode 0675 - Cut Off Trees for Golf Event
# https://leetcode.com/problems/cut-off-trees-for-golf-event/

from collections import deque
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        trees = sorted(
            (h, i, j)
            for i, row in enumerate(forest)
            for j, h in enumerate(row)
            if h > 1
        )

        def bfs(sr: int, sc: int, tr: int, tc: int) -> int:
            if sr == tr and sc == tc:
                return 0
            seen = {(sr, sc)}
            queue: deque[tuple[int, int, int]] = deque([(sr, sc, 0)])
            while queue:
                r, c, dist = queue.popleft()
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if (nr, nc) in seen or forest[nr][nc] == 0:
                        continue
                    if nr == tr and nc == tc:
                        return dist + 1
                    seen.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
            return -1

        sr = sc = steps = 0
        for _, tr, tc in trees:
            dist = bfs(sr, sc, tr, tc)
            if dist < 0:
                return -1
            steps += dist
            sr, sc = tr, tc
        return steps
