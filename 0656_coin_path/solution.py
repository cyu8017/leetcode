# LeetCode 0656 - Coin Path
# https://leetcode.com/problems/coin-path/

from typing import List


class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        if coins[-1] == -1:
            return []

        inf = 10**18
        cost = [inf] * n
        nxt = [-1] * n
        cost[-1] = coins[-1]

        for i in range(n - 2, -1, -1):
            if coins[i] == -1:
                continue
            for jump in range(1, maxJump + 1):
                j = i + jump
                if j >= n:
                    break
                if cost[j] == inf:
                    continue
                candidate = coins[i] + cost[j]
                if candidate < cost[i] or (
                    candidate == cost[i] and (nxt[i] == -1 or j < nxt[i])
                ):
                    cost[i] = candidate
                    nxt[i] = j

        if cost[0] == inf:
            return []

        path = [1]
        i = 0
        while i != n - 1:
            i = nxt[i]
            path.append(i + 1)
        return path
