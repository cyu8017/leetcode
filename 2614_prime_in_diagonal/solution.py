# LeetCode 2614 - Prime In Diagonal
# https://leetcode.com/problems/prime-in-diagonal/

from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        n = len(nums)
        best = 0
        for i in range(n):
            a, b = nums[i][i], nums[i][n - 1 - i]
            if is_prime(a) and a > best:
                best = a
            if is_prime(b) and b > best:
                best = b
        return best
