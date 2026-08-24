# LeetCode 3075 - Maximize Happiness of Selected Children
# https://leetcode.com/problems/maximize-happiness-of-selected-children/

from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        ans = 0
        for i in range(k):
            x = happiness[len(happiness) - i - 1] - i
            ans += max(x, 0)
        return ans
