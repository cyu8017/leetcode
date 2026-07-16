# LeetCode 0973 - K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return sorted(points, key=lambda p: p[0] * p[0] + p[1] * p[1])[:k]
