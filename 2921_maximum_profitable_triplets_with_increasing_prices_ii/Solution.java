// LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

class Solution {
    private int[] bit;

    public int maxProfit(int[] prices, int[] profits) {
        int n = prices.length, ans = -1;
        int[] maxLeft = new int[n];
        bit = new int[5002];
        for (int j = 0; j < n; j++) {
            maxLeft[j] = query(prices[j] - 1);
            update(prices[j], profits[j]);
        }
        for (int j = 0; j < n; j++) {
            int bestR = -1;
            for (int k = j + 1; k < n; k++)
                if (prices[k] > prices[j] && profits[k] > bestR) bestR = profits[k];
            if (maxLeft[j] >= 0 && bestR >= 0) {
                int cand = maxLeft[j] + profits[j] + bestR;
                if (cand > ans) ans = cand;
            }
        }
        return ans;
    }

    private void update(int i, int val) {
        for (; i < bit.length; i += i & -i)
            if (val > bit[i]) bit[i] = val;
    }

    private int query(int i) {
        int best = -1;
        for (; i > 0; i -= i & -i)
            if (bit[i] > best) best = bit[i];
        return best;
    }
}
