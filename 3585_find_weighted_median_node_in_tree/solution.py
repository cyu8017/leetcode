# LeetCode 3585 - Find Weighted Median Node in Tree
# https://leetcode.com/problems/find-weighted-median-node-in-tree/

from collections import deque
from typing import List


class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        ans = [0] * len(queries)
        for qi, q in enumerate(queries):
            u, v = q[0], q[1]
            parent = [-2] * n
            pw = [0] * n
            parent[u] = -1
            dq = deque([u])
            while dq:
                x = dq.popleft()
                if x == v:
                    break
                for to, w in g[x]:
                    if parent[to] == -2:
                        parent[to] = x
                        pw[to] = w
                        dq.append(to)
            nodes = [v]
            weights = []
            cur = v
            while cur != u:
                weights.append(pw[cur])
                cur = parent[cur]
                nodes.append(cur)
            nodes.reverse()
            weights.reverse()
            total = sum(weights)
            need = (total + 1) // 2
            sm = 0
            med = u
            for i, w in enumerate(weights):
                sm += w
                med = nodes[i + 1]
                if sm >= need:
                    break
            ans[qi] = med
        return ans
