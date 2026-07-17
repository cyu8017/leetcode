// LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

import java.util.Arrays;

class Solution {
    public int minSkips(int[] dist, int speed, int hoursBefore) {
        long limit = (long) hoursBefore * speed;
        int n = dist.length;
        long inf = Long.MAX_VALUE / 4;
        long[] dp = new long[n + 1];
        Arrays.fill(dp, inf);
        dp[0] = 0;

        for (int road : dist) {
            long[] next = new long[n + 1];
            Arrays.fill(next, inf);
            for (int skips = 0; skips < n; skips++) {
                if (dp[skips] == inf) {
                    continue;
                }
                long withRest = ((dp[skips] + road + speed - 1) / speed) * speed;
                next[skips] = Math.min(next[skips], withRest);
                next[skips + 1] = Math.min(next[skips + 1], dp[skips] + road);
            }
            dp = next;
        }

        for (int skips = 0; skips <= n; skips++) {
            if (dp[skips] <= limit) {
                return skips;
            }
        }
        return -1;
    }
}
