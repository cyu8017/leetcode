# LeetCode 3925 - Concatenate Array With Reverse
# https://leetcode.com/problems/concatenate-array-with-reverse/

from typing import List


class Solution:
    def concatWithReverse(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[n - i - 1]
        return ans
