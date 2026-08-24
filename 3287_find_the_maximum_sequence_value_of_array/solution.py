# LeetCode 3287 - Find the Maximum Sequence Value of Array
# https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

from typing import List


class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MAX = 128
        left = [[[False] * MAX for _ in range(k + 1)] for _ in range(n + 1)]
        left[0][0][0] = True
        for i in range(n):
            for j in range(k + 1):
                for v in range(MAX):
                    if not left[i][j][v]:
                        continue
                    left[i + 1][j][v] = True
                    if j < k:
                        left[i + 1][j + 1][v | nums[i]] = True
        right = [[[False] * MAX for _ in range(k + 1)] for _ in range(n + 1)]
        right[n][0][0] = True
        for i in range(n - 1, -1, -1):
            for j in range(k + 1):
                for v in range(MAX):
                    if not right[i + 1][j][v]:
                        continue
                    right[i][j][v] = True
                    if j < k:
                        right[i][j + 1][v | nums[i]] = True
        ans = 0
        for mid in range(k, n - k + 1):
            for a in range(MAX):
                if not left[mid][k][a]:
                    continue
                for b in range(MAX):
                    if right[mid][k][b] and (a ^ b) > ans:
                        ans = a ^ b
        return ans
