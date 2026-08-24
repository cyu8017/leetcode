# LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
# https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/


def is_consec3563(a: str, b: str) -> bool:
    d = abs(ord(a) - ord(b))
    return d == 1 or d == 25


class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)
        dp = [[""] * (n + 1) for _ in range(n + 1)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length
                min_str = s[i] + dp[i + 1][j]
                for k in range(i + 1, j):
                    if is_consec3563(s[i], s[k]) and dp[i + 1][k] == "":
                        cand = dp[k + 1][j]
                        if cand < min_str:
                            min_str = cand
                dp[i][j] = min_str
        return dp[0][n]
