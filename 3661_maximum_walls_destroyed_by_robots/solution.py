# LeetCode 3661 - Maximum Walls Destroyed by Robots
# https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

from typing import List
import bisect


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        arr = sorted(zip(robots, distance))
        walls = sorted(walls)
        memo = {}

        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0
            key = (i << 1) | j
            if key in memo:
                return memo[key]
            left = arr[i][0] - arr[i][1]
            if i > 0:
                left = max(left, arr[i - 1][0] + 1)
            l = bisect.bisect_left(walls, left)
            r = bisect.bisect_left(walls, arr[i][0] + 1)
            ans = dfs(i - 1, 0) + (r - l)
            right = arr[i][0] + arr[i][1]
            if i + 1 < len(arr):
                if j == 0:
                    right = min(right, arr[i + 1][0] - arr[i + 1][1] - 1)
                else:
                    right = min(right, arr[i + 1][0] - 1)
            l = bisect.bisect_left(walls, arr[i][0])
            r = bisect.bisect_left(walls, right + 1)
            ans = max(ans, dfs(i - 1, 1) + (r - l))
            memo[key] = ans
            return ans

        return dfs(n - 1, 1)
