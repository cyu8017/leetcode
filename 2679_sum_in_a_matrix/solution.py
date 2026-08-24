# LeetCode 2679 - Sum in a Matrix
# https://leetcode.com/problems/sum-in-a-matrix/

from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        ans = 0
        n = len(nums[0])
        for j in range(n):
            mx = 0
            for row in nums:
                mx = max(mx, row[j])
            ans += mx
        return ans
