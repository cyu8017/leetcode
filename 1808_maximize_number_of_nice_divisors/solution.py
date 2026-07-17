# LeetCode 1808 - Maximize Number of Nice Divisors
# https://leetcode.com/problems/maximize-number-of-nice-divisors/

MOD = 10**9 + 7


class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors <= 3:
            return primeFactors
        if primeFactors % 3 == 0:
            return pow(3, primeFactors // 3, MOD)
        if primeFactors % 3 == 1:
            return pow(3, primeFactors // 3 - 1, MOD) * 4 % MOD
        return pow(3, primeFactors // 3, MOD) * 2 % MOD
