# LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

from typing import List


def buildTree(n: int, edges: List[List[int]]) -> List[List[int]]:
    g = [[] for _ in range(n)]
    for e in edges:
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])
    return g


def bipartiteCount(g: List[List[int]], color: List[int]) -> List[int]:
    for i in range(len(color)):
        color[i] = -1
    q = [0]
    color[0] = 0
    cnt = [1, 0]
    qi = 0
    while qi < len(q):
        u = q[qi]
        qi += 1
        for v in g[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                cnt[color[v]] += 1
                q.append(v)
    return cnt


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        g1 = buildTree(n, edges1)
        g2 = buildTree(m, edges2)
        color1 = [0] * n
        color2 = [0] * m
        c1 = bipartiteCount(g1, color1)
        c2 = bipartiteCount(g2, color2)
        best2 = max(c2[0], c2[1])
        return [c1[color1[i]] + best2 for i in range(n)]
