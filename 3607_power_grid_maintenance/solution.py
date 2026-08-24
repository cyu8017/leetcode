# LeetCode 3607 - Power Grid Maintenance
# https://leetcode.com/problems/power-grid-maintenance/

from typing import List


class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        parent = list(range(c + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                if ra < rb:
                    parent[rb] = ra
                else:
                    parent[ra] = rb

        for e in connections:
            unite(e[0], e[1])
        online = [True] * (c + 1)
        comp = {}
        for i in range(1, c + 1):
            r = find(i)
            comp.setdefault(r, []).append(i)
        for ids in comp.values():
            ids.sort()
        ptr = {}
        ans = []
        for q in queries:
            t, x = q[0], q[1]
            if t == 2:
                online[x] = False
                continue
            if online[x]:
                ans.append(x)
                continue
            r = find(x)
            ids = comp[r]
            p = ptr.get(r, 0)
            while p < len(ids) and not online[ids[p]]:
                p += 1
            ptr[r] = p
            ans.append(ids[p] if p < len(ids) else -1)
        return ans
