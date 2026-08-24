# LeetCode 2340 - Minimum Adjacent Swaps to Make a Valid Array
# https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/

from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        min_i = max_i = 0
        for i in range(1, n):
            if nums[i] < nums[min_i]:
                min_i = i
            if nums[i] >= nums[max_i]:
                max_i = i
        ans = min_i + (n - 1 - max_i)
        if min_i > max_i:
            ans -= 1
        return ans
