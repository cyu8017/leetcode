# LeetCode 3649 - Number of Perfect Pairs
# https://leetcode.com/problems/number-of-perfect-pairs/

from typing import List


class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        n = len(nums)
        abs_nums = sorted(abs(x) for x in nums)
        ans = 0
        j = 0
        for i in range(n):
            if j < i + 1:
                j = i + 1
            while j < n and abs_nums[j] <= 2 * abs_nums[i]:
                j += 1
            ans += j - i - 1
        return ans
