# LeetCode 3201 - Find the Maximum Length of Valid Subsequence I
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        k = 2
        f = [[0] * k for _ in range(k)]
        ans = 0
        for raw in nums:
            x = raw % k
            for j in range(k):
                y = (j - x + k) % k
                f[x][y] = f[y][x] + 1
                ans = max(ans, f[x][y])
        return ans
