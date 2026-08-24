# LeetCode 2760 - Longest Even Odd Subarray With Threshold
# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 != 0 or nums[i] > threshold:
                continue
            j = i
            while j + 1 < n and nums[j + 1] <= threshold and nums[j + 1] % 2 != nums[j] % 2:
                j += 1
            ans = max(ans, j - i + 1)
        return ans
