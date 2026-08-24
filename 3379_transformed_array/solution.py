# LeetCode 3379 - Transformed Array
# https://leetcode.com/problems/transformed-array/

from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            j = ((i + nums[i]) % n + n) % n
            ans[i] = nums[j]
        return ans
