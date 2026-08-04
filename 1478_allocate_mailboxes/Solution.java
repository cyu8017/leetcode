// LeetCode 1478 - Allocate Mailboxes
// https://leetcode.com/problems/allocate-mailboxes/

import java.util.*;

class Solution {
    public int minDistance(int[] houses, int k) {
        Arrays.sort(houses);
        int n = houses.length;
        int[][] cost = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int mid = houses[(i + j) / 2];
                int c = 0;
                for (int t = i; t <= j; t++) c += Math.abs(houses[t] - mid);
                cost[i][j] = c;
            }
        }
        long inf = (long) 1e15;
        long[] dp = new long[n + 1];
        Arrays.fill(dp, inf);
        dp[0] = 0;
        for (int box = 0; box < k; box++) {
            long[] ndp = new long[n + 1];
            Arrays.fill(ndp, inf);
            for (int j = 1; j <= n; j++) {
                for (int i = 0; i < j; i++) {
                    ndp[j] = Math.min(ndp[j], dp[i] + cost[i][j - 1]);
                }
            }
            dp = ndp;
        }
        return (int) dp[n];
    }
}
