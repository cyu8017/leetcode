import bisect
class Solution:
    def maxValue(self, events, k):
        events.sort(key=lambda x: x[1])
        ends = [e[1] for e in events]
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            j = bisect.bisect_right(ends, events[i][0] - 1)
            for c in range(1, k + 1):
                dp[i][c] = max(dp[i + 1][c], events[i][2] + dp[j][c - 1])
        return dp[0][k]
