class Solution:
    def ways(self, pizza, k):
        mod = 1_000_000_007
        rows, cols = len(pizza), len(pizza[0])
        apples = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                apples[r][c] = (pizza[r][c] == "A") + apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1]
        dp = [[1 if apples[r][c] else 0 for c in range(cols)] for r in range(rows)]
        for _ in range(1, k):
            nxt = [[0] * cols for _ in range(rows)]
            for r in range(rows):
                for c in range(cols):
                    for nr in range(r + 1, rows):
                        if apples[r][c] > apples[nr][c]:
                            nxt[r][c] += dp[nr][c]
                    for nc in range(c + 1, cols):
                        if apples[r][c] > apples[r][nc]:
                            nxt[r][c] += dp[r][nc]
                    nxt[r][c] %= mod
            dp = nxt
        return dp[0][0]
