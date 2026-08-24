# LeetCode 2398 - Maximum Number of Robots Within Budget
# https://leetcode.com/problems/maximum-number-of-robots-within-budget/

from typing import List


class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        left = 0
        s = 0
        dq = []
        ans = 0
        for right in range(n):
            while dq and chargeTimes[dq[-1]] <= chargeTimes[right]:
                dq.pop()
            dq.append(right)
            s += runningCosts[right]
            while left <= right and chargeTimes[dq[0]] + (right - left + 1) * s > budget:
                if dq[0] == left:
                    dq.pop(0)
                s -= runningCosts[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
