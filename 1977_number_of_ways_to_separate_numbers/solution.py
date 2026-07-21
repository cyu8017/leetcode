class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        if num[0] == "0":
            return 0

        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

        def le(a: int, b: int, length: int) -> bool:
            common = lcp[a][b]
            if common >= length:
                return True
            return num[a + common] < num[b + common]

        # dp[i][l] = ways to split num[:i] ending with length-l number
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        pref = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for l in range(1, i + 1):
                start = i - l
                if num[start] == "0":
                    dp[i][l] = 0
                elif start == 0:
                    dp[i][l] = 1
                else:
                    ways = pref[start][min(l - 1, start)] if l > 1 else 0
                    if start >= l and le(start - l, start, l):
                        ways = (ways + dp[start][l]) % MOD
                    dp[i][l] = ways
            for l in range(1, n + 1):
                pref[i][l] = (pref[i][l - 1] + (dp[i][l] if l <= i else 0)) % MOD

        return pref[n][n]
