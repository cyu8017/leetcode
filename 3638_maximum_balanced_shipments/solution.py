# LeetCode 3638 - Maximum Balanced Shipments
# https://leetcode.com/problems/maximum-balanced-shipments/

from typing import List


class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        ans = 0
        mx = 0
        for x in weight:
            mx = max(mx, x)
            if x < mx:
                ans += 1
                mx = 0
        return ans
