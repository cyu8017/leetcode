# LeetCode 0256 - Paint House
# https://leetcode.com/problems/paint-house/

from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        previous = costs[0][:]
        for row in range(1, len(costs)):
            previous = [
                costs[row][0] + min(previous[1], previous[2]),
                costs[row][1] + min(previous[0], previous[2]),
                costs[row][2] + min(previous[0], previous[1]),
            ]
        return min(previous)
