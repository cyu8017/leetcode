# LeetCode 3594 - Minimum Time to Transport All Individuals
# https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

from typing import List


class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        t = sorted(time)
        total = 0.0
        stage = 0
        left = n
        while left > 0:
            take = min(k, left)
            slow = t[left - 1]
            total += slow * mul[stage % m]
            left -= take
            stage += 1
            if left > 0:
                total += t[0] * mul[stage % m]
                stage += 1
        return total
