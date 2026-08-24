# LeetCode 3244 - Shortest Distance After Road Addition Queries II
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        nxt = [i + 1 for i in range(n - 1)]
        cnt = n - 1
        ans = []
        for q in queries:
            u, v = q[0], q[1]
            if nxt[u] > 0 and nxt[u] < v:
                i = nxt[u]
                while i < v:
                    cnt -= 1
                    ni = nxt[i]
                    nxt[i] = 0
                    i = ni
                nxt[u] = v
            ans.append(cnt)
        return ans
