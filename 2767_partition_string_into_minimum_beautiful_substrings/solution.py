# LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
# https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        pow5 = set()
        x = 1
        while True:
            b = bin(x)[2:]
            if len(b) > n:
                break
            pow5.add(b)
            x *= 5
        INF = 10**9
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == INF or s[i] == "0":
                continue
            for j in range(i + 1, n + 1):
                if s[i:j] in pow5:
                    dp[j] = min(dp[j], dp[i] + 1)
        return -1 if dp[n] == INF else dp[n]
