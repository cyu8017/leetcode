# LeetCode 2707 - Extra Characters in a String
# https://leetcode.com/problems/extra-characters-in-a-string/

from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dct = set(dictionary)
        n = len(s)
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(n):
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
            for j in range(i + 1, n + 1):
                if s[i:j] in dct:
                    dp[j] = min(dp[j], dp[i])
        return dp[n]
