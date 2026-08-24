# LeetCode 2144 - Minimum Cost of Buying Candies With Discount
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

from typing import List
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        arr = sorted(cost, reverse=True)
        ans = 0
        for i in range(len(arr)):
            if i % 3 != 2:
                ans += arr[i]
        return ans
