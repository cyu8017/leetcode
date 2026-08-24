# LeetCode 2360 - Longest Cycle in a Graph
# https://leetcode.com/problems/longest-cycle-in-a-graph/

from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        vis = [False] * n
        ans = -1
        for i in range(n):
            if vis[i]:
                continue
            dist = {}
            cur, step = i, 0
            while cur != -1 and not vis[cur]:
                vis[cur] = True
                dist[cur] = step
                cur = edges[cur]
                step += 1
            if cur != -1 and cur in dist:
                ans = max(ans, step - dist[cur])
        return ans
