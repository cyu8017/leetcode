// LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

public class Solution {
    public int MaxProfit(int[] prices, int[] profits) {
        int n = prices.Length, ans = -1;
        int[] maxLeft = new int[n], bit = new int[5002];
        for (int i = 0; i < n; i++) maxLeft[i] = -1;

        void Update(int i, int val) {
            for (; i < bit.Length; i += i & -i)
                if (val > bit[i]) bit[i] = val;
        }
        int Query(int i) {
            int best = -1;
            for (; i > 0; i -= i & -i)
                if (bit[i] > best) best = bit[i];
            return best;
        }

        for (int j = 0; j < n; j++) {
            maxLeft[j] = Query(prices[j] - 1);
            Update(prices[j], profits[j]);
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
}
