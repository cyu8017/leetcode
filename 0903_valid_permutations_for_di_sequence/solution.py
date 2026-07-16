# LeetCode 0903 - Valid Permutations for DI Sequence
# https://leetcode.com/problems/valid-permutations-for-di-sequence/

class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [1] * (n + 1)
        for i in range(1, n + 1):
            new_dp = [0] * (n + 1)
            if s[i - 1] == "I":
                postfix = 0
                for j in range(n - i, -1, -1):
                    postfix = (postfix + dp[j + 1]) % MOD
                    new_dp[j] = postfix
            else:
                prefix = 0
                for j in range(n - i + 1):
                    prefix = (prefix + dp[j]) % MOD
                    new_dp[j] = prefix
            dp = new_dp
        return dp[0]
