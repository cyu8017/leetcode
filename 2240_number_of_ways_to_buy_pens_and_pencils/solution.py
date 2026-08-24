# LeetCode 2240 - Number of Ways to Buy Pens and Pencils
# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        pens = 0
        while pens * cost1 <= total:
            remain = total - pens * cost1
            ans += remain // cost2 + 1
            pens += 1
        return ans
