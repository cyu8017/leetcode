# LeetCode 3161 - Block Placement Queries
# https://leetcode.com/problems/block-placement-queries/

import bisect
from typing import List


class FenwickMax:
    def __init__(self, n: int):
        self.vals = [0] * (n + 1)

    def maximize(self, i: int, val: int) -> None:
        while i < len(self.vals):
            self.vals[i] = max(self.vals[i], val)
            i += i & -i

    def get(self, i: int) -> int:
        res = 0
        while i > 0:
            res = max(res, self.vals[i])
            i -= i & -i
        return res


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        n = len(queries) * 3
        if n > 50000:
            n = 50000
        tree = FenwickMax(n + 1)
        obs = [0, n]
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = bisect.bisect_left(obs, x)
                if idx == len(obs) or obs[idx] != x:
                    obs.insert(idx, x)
        for i in range(len(obs) - 1):
            tree.maximize(obs[i + 1], obs[i + 1] - obs[i])
        ans = []
        for i in range(len(queries) - 1, -1, -1):
            typ, x = queries[i][0], queries[i][1]
            if typ == 1:
                j = bisect.bisect_left(obs, x)
                prev, nxt = obs[j - 1], obs[j + 1]
                obs.pop(j)
                tree.maximize(nxt, nxt - prev)
            else:
                sz = queries[i][2]
                j = bisect.bisect_left(obs, x + 1) - 1
                prev = obs[j]
                ans.append(tree.get(prev) >= sz or x - prev >= sz)
        ans.reverse()
        return ans
