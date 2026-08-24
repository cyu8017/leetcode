# LeetCode 2517 - Maximum Tastiness of Candy Basket
# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price = sorted(price)

        def ok(d: int) -> bool:
            cnt = 1
            last = price[0]
            for i in range(1, len(price)):
                if price[i] - last >= d:
                    cnt += 1
                    last = price[i]
                    if cnt >= k:
                        return True
            return False

        lo, hi = 0, price[-1] - price[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
