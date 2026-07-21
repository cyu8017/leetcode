// LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

public class Solution {
    public int MinSkips(int[] dist, int speed, int hoursBefore) {
        long limit = (long)hoursBefore * speed;
        int n = dist.Length;
        const long INF = long.MaxValue / 4;
        var dp = new long[n + 1];
        Array.Fill(dp, INF);
        dp[0] = 0;

        foreach (int road in dist) {
            var nxt = new long[n + 1];
            Array.Fill(nxt, INF);
            for (int skips = 0; skips < n; skips++) {
                if (dp[skips] >= INF) {
                    continue;
                }
                long ceiled = ((dp[skips] + road + speed - 1) / speed) * speed;
                nxt[skips] = Math.Min(nxt[skips], ceiled);
                nxt[skips + 1] = Math.Min(nxt[skips + 1], dp[skips] + road);
            }
            dp = nxt;
        }

        for (int skips = 0; skips <= n; skips++) {
            if (dp[skips] <= limit) {
                return skips;
            }
        }
        return -1;
    }
}
