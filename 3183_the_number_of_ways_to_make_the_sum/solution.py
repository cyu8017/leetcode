# LeetCode 3183 - The Number of Ways to Make the Sum
# https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/


class Solution:
    def numberOfWays(self, n: int) -> int:
        mod = 1000000007
        coins = [1, 2, 6]
        f = [0] * (n + 1)
        f[0] = 1
        for x in coins:
            for j in range(x, n + 1):
                f[j] = (f[j] + f[j - x]) % mod
        ans = f[n]
        if n >= 4:
            ans = (ans + f[n - 4]) % mod
        if n >= 8:
            ans = (ans + f[n - 8]) % mod
        return ans
