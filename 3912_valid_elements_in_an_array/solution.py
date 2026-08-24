# LeetCode 3912 - Valid Elements In An Array
# https://leetcode.com/problems/valid-elements-in-an-array/

from typing import List


class Solution:
    def findValidElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], nums[i])
        left = 0
        ans: List[int] = []
        for i in range(n):
            x = nums[i]
            if x > left or i == n - 1 or x > right[i + 1]:
                ans.append(x)
            left = max(left, x)
        return ans
