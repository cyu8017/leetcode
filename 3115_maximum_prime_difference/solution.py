# LeetCode 3115 - Maximum Prime Difference
# https://leetcode.com/problems/maximum-prime-difference/

from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True

        i = 0
        while True:
            if is_prime(nums[i]):
                j = len(nums) - 1
                while True:
                    if is_prime(nums[j]):
                        return j - i
                    j -= 1
            i += 1
