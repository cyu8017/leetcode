# LeetCode 2778 - Sum of Squares of Special Elements
# https://leetcode.com/problems/sum-of-squares-of-special-elements/

from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if n % (i + 1) == 0:
                ans += nums[i] * nums[i]
        return ans
