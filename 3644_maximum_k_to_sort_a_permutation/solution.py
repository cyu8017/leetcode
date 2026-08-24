# LeetCode 3644 - Maximum K to Sort a Permutation
# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1
        for i, v in enumerate(nums):
            if i != v:
                ans &= v
        return max(ans, 0)
