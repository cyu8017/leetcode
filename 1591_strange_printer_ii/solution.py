from typing import List

from collections import defaultdict, deque

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        colors = {x for row in targetGrid for x in row}
        bounds = {c: [10**9, 10**9, -1, -1] for c in colors}
        for r, row in enumerate(targetGrid):
            for col, c in enumerate(row):
                b = bounds[c]
                b[0], b[1], b[2], b[3] = min(b[0], r), min(b[1], col), max(b[2], r), max(b[3], col)
        graph, indegree = defaultdict(set), {c: 0 for c in colors}
        for c, (r1, c1, r2, c2) in bounds.items():
            for r in range(r1, r2 + 1):
                for col in range(c1, c2 + 1):
                    other = targetGrid[r][col]
                    if other != c and other not in graph[c]:
                        graph[c].add(other)
                        indegree[other] += 1
        queue = deque(c for c in colors if indegree[c] == 0)
        seen = 0
        while queue:
            c = queue.popleft()
            seen += 1
            for nxt in graph[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return seen == len(colors)
