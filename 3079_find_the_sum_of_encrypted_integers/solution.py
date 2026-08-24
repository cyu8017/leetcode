# LeetCode 3079 - Find the Sum of Encrypted Integers
# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(x: int) -> int:
            mx = 0
            p = 0
            while x > 0:
                mx = max(mx, x % 10)
                p = p * 10 + 1
                x = x // 10
            return mx * p

        ans = 0
        for x in nums:
            ans += encrypt(x)
        return ans
