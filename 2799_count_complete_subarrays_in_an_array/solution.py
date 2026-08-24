# LeetCode 2799 - Count Complete Subarrays in an Array
# https://leetcode.com/problems/count-complete-subarrays-in-an-array/

from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        need = len(set(nums))
        ans = 0
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                if len(seen) == need:
                    ans += n - j
                    break
        return ans
