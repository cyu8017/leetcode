# LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                nums = [grid[x][y] for x in range(i, i + k) for y in range(j, j + k)]
                nums.sort()
                d = 2147483647
                for t in range(1, len(nums)):
                    if nums[t] != nums[t - 1]:
                        d = min(d, abs(nums[t] - nums[t - 1]))
                if d != 2147483647:
                    ans[i][j] = d
        return ans
