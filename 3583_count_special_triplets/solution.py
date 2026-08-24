# LeetCode 3583 - Count Special Triplets
# https://leetcode.com/problems/count-special-triplets/

from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left = {}
        right = {}
        for x in nums:
            right[x] = right.get(x, 0) + 1
        ans = 0
        mod = 1000000007
        for x in nums:
            right[x] -= 1
            lv = left.get(x * 2, 0)
            rv = right.get(x * 2, 0)
            ans = (ans + lv * rv % mod) % mod
            left[x] = left.get(x, 0) + 1
        return ans
