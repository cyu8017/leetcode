# LeetCode 3101 - Count Alternating Subarrays
# https://leetcode.com/problems/count-alternating-subarrays/

from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = 1
        s = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                s += 1
            else:
                s = 1
            ans += s
        return ans
