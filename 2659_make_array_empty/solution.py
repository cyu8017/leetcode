# LeetCode 2659 - Make Array Empty
# https://leetcode.com/problems/make-array-empty/

from typing import List


class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        idx = list(range(n))
        idx.sort(key=lambda i: nums[i])
        ans = n
        for i in range(1, n):
            if idx[i] < idx[i - 1]:
                ans += n - i
        return ans
