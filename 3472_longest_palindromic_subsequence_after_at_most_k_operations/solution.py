# LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
# https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/


class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(n)]

        def dist_circ(a: str, b: str) -> int:
            d = abs(ord(a) - ord(b))
            return min(d, 26 - d)

        def dfs(i: int, j: int, ops: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1
            if dp[i][j][ops] != -1:
                return dp[i][j][ops]
            best = dfs(i + 1, j, ops)
            best = max(best, dfs(i, j - 1, ops))
            cost = dist_circ(s[i], s[j])
            if cost <= ops:
                best = max(best, 2 + dfs(i + 1, j - 1, ops - cost))
            dp[i][j][ops] = best
            return best

        return dfs(0, n - 1, k)
