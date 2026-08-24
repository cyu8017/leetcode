# LeetCode 2470 - Number of Subarrays With LCM Equal to K
# https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

from typing import List


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        ans = 0
        n = len(nums)
        for i in range(n):
            cur = 1
            for j in range(i, n):
                cur = (cur // gcd(cur, nums[j])) * nums[j]
                if cur > k:
                    break
                if cur == k:
                    ans += 1
        return ans
