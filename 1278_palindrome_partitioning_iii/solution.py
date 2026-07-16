class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = (cost[i + 1][j - 1] if length > 2 else 0) + (s[i] != s[j])
        inf = n + 1
        dp = [[inf] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for parts in range(1, k + 1):
            for end in range(parts, n + 1):
                dp[parts][end] = min(dp[parts - 1][start] + cost[start][end - 1]
                                     for start in range(parts - 1, end))
        return dp[k][n]
