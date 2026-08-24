# LeetCode 2110 - Number of Smooth Descent Periods of a Stock
# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = cur = 1
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                cur += 1
            else:
                cur = 1
            ans += cur
        return ans
