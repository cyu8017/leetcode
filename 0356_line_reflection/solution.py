# LeetCode 0356 - Line Reflection
# https://leetcode.com/problems/line-reflection/

from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        point_set = {(x, y) for x, y in points}
        xs = [x for x, _ in points]
        min_x = min(xs)
        max_x = max(xs)
        target = min_x + max_x

        for x, y in points:
            if (target - x, y) not in point_set:
                return False

        return True
