# LeetCode 3068 - Find the Maximum Sum of Node Values
# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        f0 = 0
        f1 = -(1 << 53)
        for x in nums:
            nf0 = max(f0 + x, f1 + (x ^ k))
            nf1 = max(f1 + x, f0 + (x ^ k))
            f0 = nf0
            f1 = nf1
        return f0
