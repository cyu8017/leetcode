# LeetCode 3809 - Best Reachable Tower
# https://leetcode.com/problems/best-reachable-tower/

from typing import List


class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        cx, cy = center[0], center[1]
        idx = -1
        for i, (x, y, q) in enumerate(towers):
            dist = abs(x - cx) + abs(y - cy)
            if dist > radius:
                continue
            if (idx == -1 or towers[idx][2] < q or
                    (towers[idx][2] == q and
                     (x < towers[idx][0] or (x == towers[idx][0] and y < towers[idx][1])))):
                idx = i
        if idx == -1:
            return [-1, -1]
        return [towers[idx][0], towers[idx][1]]
