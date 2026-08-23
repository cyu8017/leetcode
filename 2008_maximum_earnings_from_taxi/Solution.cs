// LeetCode 2008 - Maximum Earnings From Taxi
// https://leetcode.com/problems/maximum-earnings-from-taxi/

using System;

public class Solution {
    public long MaxTaxiEarnings(int n, int[][] rides) {
        Array.Sort(rides, (a, b) => a[1].CompareTo(b[1]));
        int m = rides.Length;
        int[] ends = new int[m];
        for (int i = 0; i < m; i++) ends[i] = rides[i][1];
        long[] dp = new long[m + 1];
        for (int i = 0; i < m; i++) {
            int start = rides[i][0], end = rides[i][1], tip = rides[i][2];
            long earn = (long)end - start + tip;
            int lo = 0, hi = m;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (ends[mid] <= start) lo = mid + 1;
                else hi = mid;
            }
            dp[i + 1] = Math.Max(dp[i], earn + dp[lo]);
        }
        return dp[m];
    }
}
