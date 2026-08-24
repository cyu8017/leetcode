# LeetCode 3310 - Remove Methods From Project
# https://leetcode.com/problems/remove-methods-from-project/

from typing import List


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for e in invocations:
            g[e[0]].append(e[1])
        sus = [False] * n

        def dfs(u: int) -> None:
            if sus[u]:
                return
            sus[u] = True
            for v in g[u]:
                dfs(v)

        dfs(k)
        for e in invocations:
            if (not sus[e[0]]) and sus[e[1]]:
                return list(range(n))
        return [i for i in range(n) if not sus[i]]
