# LeetCode 2076 - Process Restricted Friend Requests
# https://leetcode.com/problems/process-restricted-friend-requests/

from typing import List


class Solution:
    def friendRequests(
        self, n: int, restrictions: List[List[int]], requests: List[List[int]]
    ) -> List[bool]:
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a: int, b: int) -> None:
            a, b = find(a), find(b)
            if a != b:
                parent[a] = b

        ans = [False] * len(requests)
        for i, (ru, rv) in enumerate(requests):
            u, v = find(ru), find(rv)
            ok = True
            if u != v:
                for x0, y0 in restrictions:
                    x, y = find(x0), find(y0)
                    if (x == u and y == v) or (x == v and y == u):
                        ok = False
                        break
            ans[i] = ok
            if ok:
                unite(u, v)
        return ans
