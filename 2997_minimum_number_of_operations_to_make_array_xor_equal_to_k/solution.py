# LeetCode 2997 - Minimum Number of Operations to Make Array XOR Equal to K
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xorr = 0
        for v in nums:
            xorr ^= v
        diff = xorr ^ k
        ans = 0
        while diff > 0:
            ans += diff & 1
            diff >>= 1
        return ans
