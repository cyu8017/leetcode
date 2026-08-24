# LeetCode 3976 - Maximum Subarray Sum After Multiplier
# https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/

from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        inf = -(2 ** 53) // 4
        f = [[inf] * 4 for _ in range(n + 1)]
        f[0][0] = 0
        ans = inf
        for i in range(1, n + 1):
            x = nums[i - 1]
            f[i][0] = max(f[i - 1][0], 0) + x
            f[i][1] = max(max(f[i - 1][0], f[i - 1][1]), 0) + x * k
            f[i][2] = max(max(f[i - 1][0], f[i - 1][2]), 0) + int(x / k)
            f[i][3] = max(max(f[i - 1][1], f[i - 1][2]), f[i - 1][3]) + x
            ans = max(ans, max(max(f[i][0], f[i][1]), max(f[i][2], f[i][3])))
        return ans
