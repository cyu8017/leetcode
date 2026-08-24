# LeetCode 3331 - Find Subtree Sizes After Changes
# https://leetcode.com/problems/find-subtree-sizes-after-changes/

from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
        new_parent = parent[:]
        last = [-1] * 26

        def dfs1(u: int) -> None:
            c = ord(s[u]) - 97
            prev = last[c]
            if prev != -1:
                new_parent[u] = prev
            last[c] = u
            for v in g[u]:
                dfs1(v)
            last[c] = prev

        dfs1(0)
        ng = [[] for _ in range(n)]
        for i in range(1, n):
            ng[new_parent[i]].append(i)
        ans = [0] * n

        def dfs2(u: int) -> int:
            sz = 1
            for v in ng[u]:
                sz += dfs2(v)
            ans[u] = sz
            return sz

        dfs2(0)
        return ans
