# LeetCode 2361 - Minimum Costs Using the Train Line
# https://leetcode.com/problems/minimum-costs-using-the-train-line/

from typing import List


class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)
        ans = [0] * n
        reg, exp = 0, expressCost
        for i in range(n):
            next_reg = min(reg + regular[i], exp + express[i])
            next_exp = min(reg + regular[i] + expressCost, exp + express[i])
            reg, exp = next_reg, next_exp
            ans[i] = min(reg, exp)
        return ans
