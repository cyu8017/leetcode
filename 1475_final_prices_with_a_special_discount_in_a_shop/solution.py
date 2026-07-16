from typing import List, Optional

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans, stack = prices[:], []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                j = stack.pop(); ans[j] -= price
            stack.append(i)
        return ans
