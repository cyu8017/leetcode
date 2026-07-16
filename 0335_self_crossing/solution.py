# LeetCode 0335 - Self Crossing
# https://leetcode.com/problems/self-crossing/

from typing import List


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        for index in range(3, len(distance)):
            if distance[index] >= distance[index - 2] and distance[index - 1] <= distance[index - 3]:
                return True
            if index >= 4 and distance[index - 1] == distance[index - 3]:
                if distance[index - 2] >= distance[index - 4] + distance[index]:
                    return True
            if index >= 5:
                if distance[index - 4] >= distance[index - 2] - distance[index]:
                    if distance[index] >= distance[index - 2] - distance[index - 4]:
                        if distance[index - 1] <= distance[index - 3]:
                            if distance[index - 5] + distance[index - 1] >= distance[index - 3]:
                                return True
        return False
