# LeetCode 3300 - Minimum Element After Replacement With Digit Sum
# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = 1000000000
        for num in nums:
            x, s = num, 0
            while x > 0:
                s += x % 10
                x //= 10
            if s < ans:
                ans = s
        return ans
