# LeetCode 3018 - Maximum Number of Removal Queries That Can Be Processed I
# https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

from typing import List


class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        m = len(queries)
        for i in range(n):
            for j in range(n - 1, i - 1, -1):
                if i > 0:
                    t = 1 if f[i - 1][j] < m and nums[i - 1] >= queries[f[i - 1][j]] else 0
                    f[i][j] = max(f[i][j], f[i - 1][j] + t)
                if j + 1 < n:
                    t = 1 if f[i][j + 1] < m and nums[j + 1] >= queries[f[i][j + 1]] else 0
                    f[i][j] = max(f[i][j], f[i][j + 1] + t)
                if f[i][j] == m:
                    return m
        ans = 0
        for i in range(n):
            t = 1 if f[i][i] < m and nums[i] >= queries[f[i][i]] else 0
            ans = max(ans, f[i][i] + t)
        return ans
