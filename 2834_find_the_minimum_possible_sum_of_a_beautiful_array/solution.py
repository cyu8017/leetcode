# LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
# https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/


class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        MOD = 1000000007
        m = target // 2
        if n <= m:
            return (n * (n + 1) // 2) % MOD
        total = m * (m + 1) // 2
        remain = n - m
        total += remain * target + remain * (remain - 1) // 2
        return total % MOD
