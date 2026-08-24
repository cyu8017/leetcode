# LeetCode 3946 - Maximum Number Of Items From Sale I
# https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        f = [0] * (budget + 1)
        mn = 2147483647
        for item in items:
            factor, price = item[0], item[1]
            mn = min(mn, price)
            cnt = 0
            for j_item in items:
                if j_item[0] % factor == 0:
                    cnt += 1
            for j in range(budget, price - 1, -1):
                f[j] = max(f[j], f[j - price] + cnt)
        ans = 0
        for i in range(budget + 1):
            extra = (budget - i) // mn
            ans = max(ans, f[i] + extra)
        return ans
