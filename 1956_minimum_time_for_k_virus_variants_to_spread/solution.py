from typing import List

class Solution:
    def minDayskVariants(self, points: List[List[int]], k: int) -> int:
        # Constraints: coordinates in [1, 100]. Brute force candidate infection points.
        ans = float('inf')
        for x in range(1, 101):
            for y in range(1, 101):
                dists = [abs(px - x) + abs(py - y) for px, py in points]
                dists.sort()
                ans = min(ans, dists[k - 1])
        return ans
