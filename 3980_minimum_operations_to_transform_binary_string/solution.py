# LeetCode 3980 - Minimum Operations to Transform Binary String
# https://leetcode.com/problems/minimum-operations-to-transform-binary-string/


class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        infinity = 1000000000
        dp = [0, infinity]
        n = len(s1)
        for i in range(n):
            nxt = [infinity, infinity]
            for forced_zero in range(2):
                if dp[forced_zero] == infinity:
                    continue
                current = s1[i]
                if forced_zero == 1:
                    current = "0"
                direct = dp[forced_zero]
                if current == "0" and s2[i] == "1":
                    direct += 1
                elif current == "1" and s2[i] == "0":
                    direct = infinity
                nxt[0] = min(nxt[0], direct)
                if i + 1 < n:
                    cost = dp[forced_zero] + 1
                    if current == "0":
                        cost += 1
                    if s1[i + 1] == "0":
                        cost += 1
                    if s2[i] == "1":
                        cost += 1
                    nxt[1] = min(nxt[1], cost)
            dp = nxt
        return -1 if dp[0] == infinity else dp[0]
