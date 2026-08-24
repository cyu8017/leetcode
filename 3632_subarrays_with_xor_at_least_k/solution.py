# LeetCode 3632 - Subarrays With XOR At Least K
# https://leetcode.com/problems/subarrays-with-xor-at-least-k/

from typing import List


class Solution:
    def subarraysWithXorAtLeastK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            x = 0
            for j in range(i, n):
                x ^= nums[j]
                if x >= k:
                    ans += 1
        return ans
