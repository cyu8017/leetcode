# LeetCode 1133 - Largest Unique Number
# https://leetcode.com/problems/largest-unique-number/

from collections import Counter


class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        count = Counter(nums)
        ans = -1
        for value, freq in count.items():
            if freq == 1:
                ans = max(ans, value)
        return ans
