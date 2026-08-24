# LeetCode 2366 - Minimum Replacements to Sort the Array
# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        prev = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
                continue
            parts = (nums[i] + prev - 1) // prev
            ans += parts - 1
            prev = nums[i] // parts
        return ans
