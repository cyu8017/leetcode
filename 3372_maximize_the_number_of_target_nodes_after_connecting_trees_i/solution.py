# LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

from typing import List


def buildTree(n: int, edges: List[List[int]]) -> List[List[int]]:
    g = [[] for _ in range(n)]
    for e in edges:
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])
    return g


def countWithin(g: List[List[int]], start: int, k: int) -> int:
    if k < 0:
        return 0
    n = len(g)
    vis = [False] * n
    q = [[start, 0]]
    vis[start] = True
    cnt = 0
    qi = 0
    while qi < len(q):
        u, d = q[qi]
        qi += 1
        cnt += 1
        if d == k:
            continue
        for v in g[u]:
            if not vis[v]:
                vis[v] = True
                q.append([v, d + 1])
    return cnt


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        g1 = buildTree(n, edges1)
        g2 = buildTree(m, edges2)
        cnt1 = [countWithin(g1, i, k) for i in range(n)]
        best2 = 0
        if k > 0:
            for i in range(m):
                c = countWithin(g2, i, k - 1)
                if c > best2:
                    best2 = c
        return [cnt1[i] + best2 for i in range(n)]
