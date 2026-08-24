# LeetCode 3645 - Maximum Total from Optimal Activation Order
# https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

from typing import List


class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        g = {}
        for i, lim in enumerate(limit):
            g.setdefault(lim, []).append(value[i])
        ans = 0
        for lim, vs in g.items():
            vs.sort(reverse=True)
            ans += sum(vs[:lim])
        return ans
