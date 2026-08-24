# LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
# https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

from typing import List


class Solution:
    def maxTastiness(
        self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int
    ) -> int:
        n = len(price)
        neg = -(2147483647 // 2)
        dp = [[neg] * (maxCoupons + 1) for _ in range(maxAmount + 1)]
        dp[0][0] = 0
        for i in range(n):
            p, t = price[i], tastiness[i]
            for a in range(maxAmount, -1, -1):
                for c in range(maxCoupons, -1, -1):
                    if dp[a][c] < 0:
                        continue
                    if a + p <= maxAmount:
                        dp[a + p][c] = max(dp[a + p][c], dp[a][c] + t)
                    if c + 1 <= maxCoupons and a + p // 2 <= maxAmount:
                        half = a + p // 2
                        dp[half][c + 1] = max(dp[half][c + 1], dp[a][c] + t)
        ans = 0
        for a in range(maxAmount + 1):
            for c in range(maxCoupons + 1):
                ans = max(ans, dp[a][c])
        return ans
