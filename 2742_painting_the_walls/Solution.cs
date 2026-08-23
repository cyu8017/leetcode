// LeetCode 2742 - Painting the Walls
// https://leetcode.com/problems/painting-the-walls/

public class Solution {
    public int PaintWalls(int[] cost, int[] time) {
        int n = cost.Length;
        const long INF = 1L << 60;
        long[] dp = new long[n + 1];
        for (int i = 1; i <= n; i++) dp[i] = INF;
        for (int i = 0; i < n; i++) {
            for (int j = n; j >= 0; j--) {
                int nj = j + time[i] + 1;
                if (nj > n) nj = n;
                if (dp[j] + cost[i] < dp[nj]) dp[nj] = dp[j] + cost[i];
            }
        }
        return (int)dp[n];
    }
}
