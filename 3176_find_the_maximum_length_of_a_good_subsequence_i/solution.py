# LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [[0] * (k + 1) for _ in range(n)]
        ans = 0
        for i in range(n):
            for h in range(k + 1):
                for j in range(i):
                    if nums[i] == nums[j]:
                        f[i][h] = max(f[i][h], f[j][h])
                    elif h > 0:
                        f[i][h] = max(f[i][h], f[j][h - 1])
                f[i][h] += 1
            ans = max(ans, f[i][k])
        return ans
