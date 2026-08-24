# LeetCode 2359 - Find Closest Node to Given Two Nodes
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def dist(start: int) -> List[int]:
            d = [-1] * n
            cur, step = start, 0
            while cur != -1 and d[cur] == -1:
                d[cur] = step
                cur = edges[cur]
                step += 1
            return d

        d1, d2 = dist(node1), dist(node2)
        ans = -1
        best = float("inf")
        for i in range(n):
            if d1[i] == -1 or d2[i] == -1:
                continue
            mx = max(d1[i], d2[i])
            if mx < best:
                best = mx
                ans = i
        return ans
