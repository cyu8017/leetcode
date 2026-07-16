# LeetCode 0447 - Number of Boomerangs
# https://leetcode.com/problems/number-of-boomerangs/

from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        total = 0
        for anchor in points:
            distances: defaultdict[int, int] = defaultdict(int)
            for other in points:
                dx = anchor[0] - other[0]
                dy = anchor[1] - other[1]
                distances[dx * dx + dy * dy] += 1
            for count in distances.values():
                total += count * (count - 1)
        return total
