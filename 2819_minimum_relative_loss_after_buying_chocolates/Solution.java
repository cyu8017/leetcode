// LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
// https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

import java.util.Arrays;

class Solution {
    public long[] minimumRelativeLosses(int[] prices, int[][] queries) {
        Arrays.sort(prices);
        int n = prices.length;
        long[] ans = new long[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            int kk = queries[qi][0], m = queries[qi][1];
            long[] losses = new long[n];
            for (int i = 0; i < n; i++) {
                if (prices[i] <= kk) losses[i] = prices[i];
                else losses[i] = 2L * kk - prices[i];
            }
            Arrays.sort(losses);
            long sum = 0;
            for (int i = 0; i < m; i++) sum += losses[i];
            ans[qi] = sum;
        }
        return ans;
    }
}
