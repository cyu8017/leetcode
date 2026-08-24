# LeetCode 3249 - Count the Number of Good Nodes
# https://leetcode.com/problems/count-the-number-of-good-nodes/

from typing import List


class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        ans = 0

        def dfs(a: int, fa: int) -> int:
            nonlocal ans
            pre, cnt, ok = -1, 1, 1
            for b in g[a]:
                if b != fa:
                    cur = dfs(b, a)
                    cnt += cur
                    if pre < 0:
                        pre = cur
                    elif pre != cur:
                        ok = 0
            ans += ok
            return cnt

        dfs(0, -1)
        return ans
