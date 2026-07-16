from typing import List, Optional

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        es = sorted((w, a, b, i) for i, (a, b, w) in enumerate(edges))
        def mst(skip=-1, force=-1):
            parent = list(range(n))
            def find(x):
                while x != parent[x]:
                    parent[x] = parent[parent[x]]; x = parent[x]
                return x
            total = used = 0
            if force >= 0:
                w, a, b, _ = es[force]
                parent[find(a)] = find(b); total += w; used += 1
            for j, (w, a, b, _) in enumerate(es):
                if j == skip or j == force:
                    continue
                x, y = find(a), find(b)
                if x != y:
                    parent[x] = y; total += w; used += 1
            return total if used == n-1 else float("inf")
        base = mst()
        critical, pseudo = [], []
        for j, edge in enumerate(es):
            if mst(skip=j) > base:
                critical.append(edge[3])
            elif mst(force=j) == base:
                pseudo.append(edge[3])
        return [sorted(critical), sorted(pseudo)]
