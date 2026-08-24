# LeetCode 3730 - Maximum Calories Burnt from Jumps
# https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

from typing import List


class Solution:
    def maxCaloriesBurnt(self, heights: List[int]) -> int:
        heights = sorted(heights)
        ans = 0
        pre = 0
        l, r = 0, len(heights) - 1
        while l < r:
            d1 = heights[r] - pre
            ans += d1 * d1
            d2 = heights[l] - heights[r]
            ans += d2 * d2
            pre = heights[l]
            l += 1
            r -= 1
        d = heights[r] - pre
        ans += d * d
        return ans
