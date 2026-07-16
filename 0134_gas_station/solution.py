# LeetCode 0134 - Gas Station
# https://leetcode.com/problems/gas-station/

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = tank = start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            diff = g - c
            total += diff
            tank += diff
            if tank < 0:
                start = i + 1
                tank = 0
        return start if total >= 0 else -1
