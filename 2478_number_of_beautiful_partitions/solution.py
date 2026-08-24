# LeetCode 2478 - Number of Beautiful Partitions
# https://leetcode.com/problems/number-of-beautiful-partitions/


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        mod = 1000000007

        def is_prime(c: str) -> bool:
            return c == "2" or c == "3" or c == "5" or c == "7"

        n = len(s)
        if not is_prime(s[0]) or is_prime(s[n - 1]):
            return 0
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 1
        for p in range(1, k + 1):
            pref = 0
            j = 0
            for i in range(1, n + 1):
                while j <= i - minLength:
                    if j == 0 or (is_prime(s[j]) and not is_prime(s[j - 1])):
                        pref = (pref + dp[p - 1][j]) % mod
                    j += 1
                if not is_prime(s[i - 1]):
                    dp[p][i] = pref
        return dp[k][n]
