# LeetCode 0638 - Shopping Offers
# https://leetcode.com/problems/shopping-offers/

from functools import lru_cache
from typing import List


class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        n = len(price)

        @lru_cache(None)
        def dfs(state: tuple[int, ...]) -> int:
            cost = sum(state[i] * price[i] for i in range(n))
            for offer in special:
                nxt = list(state)
                valid = True
                for i in range(n):
                    if nxt[i] < offer[i]:
                        valid = False
                        break
                    nxt[i] -= offer[i]
                if valid:
                    cost = min(cost, offer[n] + dfs(tuple(nxt)))
            return cost

        return dfs(tuple(needs))
