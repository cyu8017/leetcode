# LeetCode 0755 - Pour Water
# https://leetcode.com/problems/pour-water/

from typing import List


class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        for _ in range(volume):
            index = k
            for i in range(k - 1, -1, -1):
                if heights[i] > heights[index]:
                    break
                if heights[i] < heights[index]:
                    index = i
            if index != k:
                heights[index] += 1
                continue

            index = k
            for i in range(k + 1, len(heights)):
                if heights[i] > heights[index]:
                    break
                if heights[i] < heights[index]:
                    index = i
            heights[index] += 1
        return heights
