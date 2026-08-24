# LeetCode 2603 - Collect Coins in a Tree
# https://leetcode.com/problems/collect-coins-in-a-tree/

from collections import deque
from typing import List


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = [set() for _ in range(n)]
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        deg = [len(g[i]) for i in range(n)]
        q = deque()
        for i in range(n):
            if deg[i] == 1 and coins[i] == 0:
                q.append(i)
        while q:
            u = q.popleft()
            for v in list(g[u]):
                g[v].discard(u)
                deg[v] -= 1
                if deg[v] == 1 and coins[v] == 0:
                    q.append(v)
            g[u].clear()
            deg[u] = 0
        for _ in range(2):
            leaves = [i for i in range(n) if deg[i] == 1]
            for u in leaves:
                for v in list(g[u]):
                    g[v].discard(u)
                    deg[v] -= 1
                g[u].clear()
                deg[u] = 0
        remain = 0
        for i in range(n):
            remain += len(g[i])
        return remain
