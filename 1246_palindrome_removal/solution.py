class Solution:
    def minimumMoves(self, arr: list[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for i in range(n): dp[i][i] = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = 1 + dp[i + 1][j]
                if arr[i] == arr[i + 1]:
                    dp[i][j] = min(dp[i][j], 1 + (dp[i + 2][j] if i + 2 <= j else 0))
                for k in range(i + 2, j + 1):
                    if arr[i] == arr[k]:
                        dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + (dp[k + 1][j] if k < j else 0))
        return dp[0][n - 1]
