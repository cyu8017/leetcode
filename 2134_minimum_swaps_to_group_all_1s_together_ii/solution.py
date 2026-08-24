# LeetCode 2134 - Minimum Swaps to Group All 1's Together II
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

from typing import List
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = 0
        for x in nums:
            ones += x
        if ones == 0:
            return 0
        n = len(nums)
        window = 0
        for i in range(ones):
            window += nums[i]
        best = window
        for i in range(n):
            window -= nums[i]
            window += nums[(i + ones) % n]
            best = max(best, window)
        return ones - best
