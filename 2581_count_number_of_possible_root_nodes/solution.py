# LeetCode 2581 - Count Number of Possible Root Nodes
# https://leetcode.com/problems/count-number-of-possible-root-nodes/

from typing import List


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        guess_set = set()

        def pack(a: int, b: int) -> str:
            return f"{a},{b}"

        for a, b in guesses:
            guess_set.add(pack(a, b))

        def dfs1(u: int, p: int) -> int:
            cnt = 0
            for v in g[u]:
                if v == p:
                    continue
                if pack(u, v) in guess_set:
                    cnt += 1
                cnt += dfs1(v, u)
            return cnt

        ans = 0

        def dfs2(u: int, p: int, cur: int) -> None:
            nonlocal ans
            if cur >= k:
                ans += 1
            for v in g[u]:
                if v == p:
                    continue
                nxt = cur
                if pack(u, v) in guess_set:
                    nxt -= 1
                if pack(v, u) in guess_set:
                    nxt += 1
                dfs2(v, u, nxt)

        base_cnt = dfs1(0, -1)
        dfs2(0, -1, base_cnt)
        return ans
