// LeetCode 2463 - Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {
        List<Integer> robots = new ArrayList<>(robot);
        Collections.sort(robots);
        Arrays.sort(factory, (a, b) -> Integer.compare(a[0], b[0]));
        int m = robots.size();
        List<Integer> pos = new ArrayList<>();
        for (int[] f : factory) {
            for (int c = 0; c < f[1]; c++) pos.add(f[0]);
        }
        int n = pos.size();
        final long INF = 1L << 60;
        long[][] dp = new long[m + 1][n + 1];
        for (int i = 0; i <= m; i++) Arrays.fill(dp[i], INF);
        for (int j = 0; j <= n; j++) dp[0][j] = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = i; j <= n; j++) {
                dp[i][j] = dp[i][j - 1];
                long diff = robots.get(i - 1) - pos.get(j - 1);
                if (diff < 0) diff = -diff;
                if (dp[i - 1][j - 1] + diff < dp[i][j]) dp[i][j] = dp[i - 1][j - 1] + diff;
            }
        }
        return dp[m][n];
    }
}
