# LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
# https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

from typing import List, Optional


class Solution:
    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        subtree = [0] * n

        def dfs_sum(u: int, p: int) -> int:
            s = values[u]
            for v in g[u]:
                if v != p:
                    s += dfs_sum(v, u)
            subtree[u] = s
            return s

        dfs_sum(0, -1)
        root = {"child": [None, None]}

        def insert(x: int) -> None:
            cur = root
            for b in range(46, -1, -1):
                bit = (x >> b) & 1
                if not cur["child"][bit]:
                    cur["child"][bit] = {"child": [None, None]}
                cur = cur["child"][bit]

        def query(x: int) -> int:
            cur = root
            if not cur["child"][0] and not cur["child"][1]:
                return 0
            res = 0
            for b in range(46, -1, -1):
                bit = (x >> b) & 1
                want = bit ^ 1
                if cur["child"][want]:
                    res |= 1 << b
                    cur = cur["child"][want]
                elif cur["child"][bit]:
                    cur = cur["child"][bit]
                else:
                    return res
            return res

        ans = 0

        def dfs(u: int, p: int) -> None:
            nonlocal ans
            for v in g[u]:
                if v == p:
                    continue
                xorv = query(subtree[v])
                if xorv > ans:
                    ans = xorv
                dfs(v, u)
                insert(subtree[v])

        dfs(0, -1)
        return ans
