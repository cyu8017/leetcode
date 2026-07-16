# LeetCode 0265 - Paint House II
# https://leetcode.com/problems/paint-house-ii/

from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        color_count = len(costs[0])
        previous = costs[0][:]
        for row in range(1, len(costs)):
            min_cost = min(previous)
            min_index = previous.index(min_cost)
            second_min = min(
                value for index, value in enumerate(previous) if index != min_index
            )
            current = []
            for color in range(color_count):
                extra = second_min if color == min_index else min_cost
                current.append(costs[row][color] + extra)
            previous = current
        return min(previous)
