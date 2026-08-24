# LeetCode 3452 - Sum of Good Numbers
# https://leetcode.com/problems/sum-of-good-numbers/

from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            x = nums[i]
            good = True
            if i - k >= 0 and x <= nums[i - k]:
                good = False
            if i + k < n and x <= nums[i + k]:
                good = False
            if good:
                ans += x
        return ans
