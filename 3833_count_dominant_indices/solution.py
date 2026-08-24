# LeetCode 3833 - Count Dominant Indices
# https://leetcode.com/problems/count-dominant-indices/

from typing import List


class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        suf = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if nums[i] * (n - i - 1) > suf:
                ans += 1
            suf += nums[i]
        return ans
