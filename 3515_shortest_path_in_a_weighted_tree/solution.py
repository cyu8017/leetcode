# LeetCode 3515 - Shortest Path in a Weighted Tree
# https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

from typing import List


class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n + 1)]
        weight = {}
        for e in edges:
            u, v, w = e[0], e[1], e[2]
            g[u].append((v, w))
            g[v].append((u, w))
            a, b = min(u, v), max(u, v)
            weight[(a << 32) | b] = w
        in_t = [0] * (n + 1)
        out_t = [0] * (n + 1)
        dist = [0] * (n + 1)
        parent = [0] * (n + 1)
        time = 0

        def dfs(u: int, p: int) -> None:
            nonlocal time
            in_t[u] = time
            time += 1
            for to, w in g[u]:
                if to == p:
                    continue
                parent[to] = u
                dist[to] = dist[u] + w
                dfs(to, u)
            out_t[u] = time - 1

        dfs(1, 0)
        bit = [0] * (n + 2)

        def add(i: int, v: int) -> None:
            while i <= n:
                bit[i] += v
                i += i & -i

        def rangeAdd(l: int, r: int, v: int) -> None:
            add(l + 1, v)
            add(r + 2, -v)

        def point(i: int) -> int:
            s = 0
            i += 1
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        for i in range(1, n + 1):
            rangeAdd(in_t[i], in_t[i], dist[i])
        ans = []
        for q in queries:
            if q[0] == 1:
                u, v, nw = q[1], q[2], q[3]
                a, b = min(u, v), max(u, v)
                key = (a << 32) | b
                ow = weight[key]
                delta = nw - ow
                weight[key] = nw
                child = u if parent[u] == v else v
                rangeAdd(in_t[child], out_t[child], delta)
            else:
                ans.append(point(in_t[q[1]]))
        return ans
