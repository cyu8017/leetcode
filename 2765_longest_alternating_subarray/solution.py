# LeetCode 2765 - Longest Alternating Subarray
# https://leetcode.com/problems/longest-alternating-subarray/

from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                expect = -1 if (j - i) % 2 == 0 else 1
                if nums[j] - nums[j - 1] != expect:
                    break
                if nums[i + 1] - nums[i] != 1:
                    break
                ans = max(ans, j - i + 1)
        return ans
