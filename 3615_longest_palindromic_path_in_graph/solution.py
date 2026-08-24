# LeetCode 3615 - Longest Palindromic Path in Graph
# https://leetcode.com/problems/longest-palindromic-path-in-graph/

from collections import deque
from typing import List


class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        def pack(a: int, b: int) -> int:
            return (a << 32) | (b & 0xFFFFFFFF)

        def expand_pal(l: int, r: int) -> int:
            vis = set()
            q = deque()
            len0 = 2 if l != r else 1
            q.append((l, r, len0))
            best = len0
            vis.add(pack(min(l, r), max(l, r)))
            while q:
                cur0, cur1, cur2 = q.popleft()
                for a in g[cur0]:
                    for b in g[cur1]:
                        if a == b or label[a] != label[b]:
                            continue
                        p = pack(min(a, b), max(a, b))
                        if p in vis:
                            continue
                        vis.add(p)
                        nl = cur2 + 2
                        best = max(best, nl)
                        q.append((a, b, nl))
            return best

        ans = 1
        for i in range(n):
            ans = max(ans, expand_pal(i, i))
            for j in g[i]:
                if i < j and label[i] == label[j]:
                    ans = max(ans, expand_pal(i, j))
        return ans
