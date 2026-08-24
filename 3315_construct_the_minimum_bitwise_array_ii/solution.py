# LeetCode 3315 - Construct the Minimum Bitwise Array II
# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        for i, n in enumerate(nums):
            if n == 2:
                continue
            for b in range(31):
                if ((n >> b) & 1) == 0:
                    continue
                x = n ^ (1 << b)
                if (x | (x + 1)) == n:
                    ans[i] = x
                    break
        return ans
