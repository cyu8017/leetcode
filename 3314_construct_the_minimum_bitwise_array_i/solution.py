# LeetCode 3314 - Construct the Minimum Bitwise Array I
# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        for i, n in enumerate(nums):
            for x in range(n):
                if (x | (x + 1)) == n:
                    ans[i] = x
                    break
        return ans
