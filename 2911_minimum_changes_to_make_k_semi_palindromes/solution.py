# LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
# https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/


class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        inf = 1 << 20
        cost = [[inf] * n for _ in range(n)]

        def semi_cost(l: int, r: int) -> int:
            length = r - l + 1
            best = inf
            for d in range(1, length):
                if length % d != 0:
                    continue
                chg = 0
                for start in range(d):
                    chars = [s[i] for i in range(l + start, r + 1, d)]
                    i, j = 0, len(chars) - 1
                    while i < j:
                        if chars[i] != chars[j]:
                            chg += 1
                        i += 1
                        j -= 1
                if chg < best:
                    best = chg
            return best

        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = semi_cost(i, j)
        dp = [[inf] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for i in range(1, n + 1):
                for t in range(i - 1):
                    cand = dp[p - 1][t] + cost[t][i - 1]
                    if cand < dp[p][i]:
                        dp[p][i] = cand
        return dp[k][n]
