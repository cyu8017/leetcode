# LeetCode 0629 - K Inverse Pairs Array
# https://leetcode.com/problems/k-inverse-pairs-array/


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1

        for size in range(1, n + 1):
            nxt = [0] * (k + 1)
            prefix = 0
            for pairs in range(k + 1):
                prefix = (prefix + dp[pairs]) % mod
                if pairs >= size:
                    prefix = (prefix - dp[pairs - size]) % mod
                nxt[pairs] = prefix
            dp = nxt

        return dp[k]
