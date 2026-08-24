# LeetCode 3277 - Maximum XOR Score Subarray Queries
# https://leetcode.com/problems/maximum-xor-score-subarray-queries/

from typing import List


class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        for i in range(n):
            f[i][i] = nums[i]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                f[i][j] = f[i][j - 1] ^ f[i + 1][j]
        best = [[0] * n for _ in range(n)]
        for i in range(n):
            best[i][i] = f[i][i]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                best[i][j] = max(f[i][j], best[i][j - 1], best[i + 1][j])
        ans = [0] * len(queries)
        for i in range(len(queries)):
            ans[i] = best[queries[i][0]][queries[i][1]]
        return ans
