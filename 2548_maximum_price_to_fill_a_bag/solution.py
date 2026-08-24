# LeetCode 2548 - Maximum Price to Fill a Bag
# https://leetcode.com/problems/maximum-price-to-fill-a-bag/

from typing import List


class Solution:
    def maxPrice(self, items: List[List[int]], capacity: int) -> float:
        items.sort(key=lambda it: -(it[0] / it[1]))
        ans = 0.0
        remain = capacity
        for price, weight in items:
            if remain >= weight:
                ans += price
                remain -= weight
            else:
                ans += price * remain / weight
                remain = 0
                break
        if remain > 0:
            return -1
        return ans
