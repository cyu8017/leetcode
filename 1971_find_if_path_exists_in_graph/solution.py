from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        stack = [source]
        seen = {source}
        while stack:
            u = stack.pop()
            if u == destination:
                return True
            for v in g[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        return False
