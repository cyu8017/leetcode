// LeetCode 1595 - Minimum Cost to Connect Two Groups of Points
// https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/

class Solution {
    public int connectTwoGroups(int[][] cost) {
        int m = cost.length;
        int n = cost[0].length;
        int full = 1 << n;
        int inf = 1_000_000_000;
        int[] dp = new int[full];
        for (int i = 0; i < full; i++) {
            dp[i] = inf;
        }
        dp[0] = 0;
        for (int[] row : cost) {
            int[] nxt = new int[full];
            for (int i = 0; i < full; i++) {
                nxt[i] = inf;
            }
            for (int mask = 0; mask < full; mask++) {
                if (dp[mask] >= inf) {
                    continue;
                }
                for (int j = 0; j < n; j++) {
                    int newMask = mask | (1 << j);
                    nxt[newMask] = Math.min(nxt[newMask], dp[mask] + row[j]);
                    nxt[newMask] = Math.min(nxt[newMask], nxt[mask] + row[j]);
                }
            }
            dp = nxt;
        }
        int[] minimum = new int[n];
        for (int j = 0; j < n; j++) {
            minimum[j] = cost[0][j];
            for (int i = 1; i < m; i++) {
                minimum[j] = Math.min(minimum[j], cost[i][j]);
            }
        }
        int ans = inf;
        for (int mask = 0; mask < full; mask++) {
            int extra = 0;
            for (int j = 0; j < n; j++) {
                if ((mask & (1 << j)) == 0) {
                    extra += minimum[j];
                }
            }
            ans = Math.min(ans, dp[mask] + extra);
        }
        return ans;
    }
}
