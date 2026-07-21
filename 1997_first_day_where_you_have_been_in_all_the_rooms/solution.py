from typing import List

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nextVisit)
        # dp[i] = first day we reach room i (0-indexed day count when arriving)
        dp = [0] * n
        for i in range(1, n):
            # From room i-1: odd visit goes to nextVisit[i-1], need even visit to go to i
            # days to go i-1 -> nextVisit[i-1] again then back to i-1 then to i
            dp[i] = (dp[i - 1] + 1 + (dp[i - 1] - dp[nextVisit[i - 1]]) + 1) % MOD
            # = (2 * dp[i-1] - dp[nextVisit[i-1]] + 2) % MOD
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD
        return dp[n - 1]
