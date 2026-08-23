// LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
// https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

using System;

public class Solution {
    public long[] MinimumRelativeLosses(int[] prices, int[][] queries) {
        Array.Sort(prices);
        int n = prices.Length;
        long[] ans = new long[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int kk = queries[qi][0], m = queries[qi][1];
            long[] losses = new long[n];
            for (int i = 0; i < n; i++) {
                if (prices[i] <= kk) losses[i] = prices[i];
                else losses[i] = 2L * kk - prices[i];
            }
            Array.Sort(losses);
            long sum = 0;
            for (int i = 0; i < m; i++) sum += losses[i];
            ans[qi] = sum;
        }
        return ans;
    }
}
