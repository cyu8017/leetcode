# LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
# https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

from typing import List


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        deg = [0] * (n + 1)
        adj = [set() for _ in range(n + 1)]
        for e in edges:
            u, v = e[0], e[1]
            deg[u] += 1
            deg[v] += 1
            adj[u].add(v)
            adj[v].add(u)
        odd = [i for i in range(1, n + 1) if deg[i] % 2 == 1]
        if not odd:
            return True
        if len(odd) == 2:
            a, b = odd[0], odd[1]
            if b not in adj[a]:
                return True
            for i in range(1, n + 1):
                if i != a and i != b and i not in adj[a] and i not in adj[b]:
                    return True
            return False
        if len(odd) == 4:
            a, b, c, d = odd
            return (
                (b not in adj[a] and d not in adj[c])
                or (c not in adj[a] and d not in adj[b])
                or (d not in adj[a] and c not in adj[b])
            )
        return False
