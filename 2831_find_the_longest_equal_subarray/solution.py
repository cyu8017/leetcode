# LeetCode 2831 - Find the Longest Equal Subarray
# https://leetcode.com/problems/find-the-longest-equal-subarray/

from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos = {}
        for i, v in enumerate(nums):
            pos.setdefault(v, []).append(i)
        ans = 0
        for p in pos.values():
            left = 0
            for right in range(len(p)):
                while p[right] - p[left] - (right - left) > k:
                    left += 1
                ans = max(ans, right - left + 1)
        return ans
