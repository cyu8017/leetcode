# LeetCode 2475 - Number of Unequal Triplets in Array
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/

from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        ans = 0
        left = 0
        n = len(nums)
        for c in cnt.values():
            right = n - left - c
            ans += left * c * right
            left += c
        return ans
