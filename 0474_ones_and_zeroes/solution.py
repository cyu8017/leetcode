# LeetCode 0474 - Ones and Zeroes
# https://leetcode.com/problems/ones-and-zeroes/


class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for string in strs:
            zeros = string.count("0")
            ones = string.count("1")
            for zero in range(m, zeros - 1, -1):
                for one in range(n, ones - 1, -1):
                    dp[zero][one] = max(
                        dp[zero][one],
                        dp[zero - zeros][one - ones] + 1,
                    )
        return dp[m][n]
