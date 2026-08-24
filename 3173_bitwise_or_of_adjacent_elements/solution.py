# LeetCode 3173 - Bitwise OR of Adjacent Elements
# https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

from typing import List


class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            ans[i - 1] = nums[i] | nums[i - 1]
        return ans
