# LeetCode 2421 - Number of Good Paths
# https://leetcode.com/problems/number-of-good-paths/

from typing import List


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        nodes = list(range(n))
        nodes.sort(key=lambda i: vals[i])
        ans = n
        i = 0
        while i < n:
            j = i
            while j < n and vals[nodes[j]] == vals[nodes[i]]:
                j += 1
            for k in range(i, j):
                u = nodes[k]
                for v in g[u]:
                    if vals[v] <= vals[u]:
                        ru, rv = find(u), find(v)
                        if ru != rv:
                            parent[ru] = rv
            freq = {}
            for k in range(i, j):
                r = find(nodes[k])
                freq[r] = freq.get(r, 0) + 1
            for c in freq.values():
                ans += c * (c - 1) // 2
            i = j
        return ans
