# LeetCode 2368 - Reachable Nodes With Restrictions
# https://leetcode.com/problems/reachable-nodes-with-restrictions/

from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        ban = set(restricted)
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        ans = 0
        vis = [False] * n
        q = [0]
        vis[0] = True
        while q:
            u = q.pop(0)
            ans += 1
            for v in g[u]:
                if not vis[v] and v not in ban:
                    vis[v] = True
                    q.append(v)
        return ans
