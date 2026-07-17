# LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
# https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

from functools import lru_cache
from typing import List


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        count = [0] * batchSize
        for size in groups:
            count[size % batchSize] += 1

        @lru_cache(maxsize=None)
        def dfs(remainder: int, state: tuple[int, ...]) -> int:
            best = 0
            state_list = list(state)
            for mod in range(1, batchSize):
                if state_list[mod] == 0:
                    continue
                state_list[mod] -= 1
                best = max(best, dfs((remainder + mod) % batchSize, tuple(state_list)))
                state_list[mod] += 1
            if remainder == 0:
                return best + 1
            return best

        ans = dfs(0, tuple(count))
        if count[0]:
            ans += count[0] - 1
        return ans
