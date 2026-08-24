# LeetCode 3317 - Find the Number of Possible Ways for an Event
# https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/


def modPow(a: int, e: int, mod: int) -> int:
    r = 1
    a %= mod
    while e > 0:
        if e & 1:
            r = r * a % mod
        a = a * a % mod
        e >>= 1
    return r


class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        mod = 1000000007
        dp = [[0] * (x + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, min(x, i) + 1):
                dp[i][j] = (dp[i - 1][j - 1] + j * dp[i - 1][j] % mod) % mod
        fact = [0] * (x + 1)
        fact[0] = 1
        for i in range(1, x + 1):
            fact[i] = fact[i - 1] * i % mod
        ans = 0
        ypow = 1
        for k in range(1, min(x, n) + 1):
            ypow = ypow * y % mod
            perm = fact[x] * modPow(fact[x - k], mod - 2, mod) % mod
            ans = (ans + dp[n][k] * perm % mod * ypow % mod) % mod
        return ans
