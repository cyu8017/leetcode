# LeetCode 2498 - Frog Jump II
# https://leetcode.com/problems/frog-jump-ii/

from typing import List


class Solution:
    def maxJump(self, stones: List[int]) -> int:
        ans = stones[1] - stones[0]
        for i in range(2, len(stones)):
            diff = stones[i] - stones[i - 2]
            if diff > ans:
                ans = diff
        return ans
