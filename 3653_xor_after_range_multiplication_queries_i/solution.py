# LeetCode 3653 - XOR After Range Multiplication Queries I
# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 1000000007
        for l, r, k, v in queries:
            for idx in range(l, r + 1, k):
                nums[idx] = nums[idx] * v % mod
        ans = 0
        for x in nums:
            ans ^= x
        return ans
