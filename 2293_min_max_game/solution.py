# LeetCode 2293 - Min Max Game
# https://leetcode.com/problems/min-max-game/

from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nxt = [0] * (len(nums) >> 1)
            for i in range(len(nxt)):
                if i % 2 == 0:
                    nxt[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    nxt[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = nxt
        return nums[0]
