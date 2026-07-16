# LeetCode 1039 - Minimum Score Triangulation of Polygon
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

from functools import lru_cache


class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if j - i < 2:
                return 0
            return min(
                dp(i, k) + values[i] * values[k] * values[j] + dp(k, j)
                for k in range(i + 1, j)
            )

        return dp(0, len(values) - 1)
