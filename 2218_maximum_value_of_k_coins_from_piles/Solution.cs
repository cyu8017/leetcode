// LeetCode 2218 - Maximum Value of K Coins From Piles
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

using System;

public class Solution {
    public int MaxValueOfCoins(IList<IList<int>> piles, int k) {
        int[] dp = new int[k + 1];
        foreach (var pile in piles) {
            int[] ndp = (int[])dp.Clone();
            int sum = 0;
            for (int take = 1; take <= pile.Count && take <= k; take++) {
                sum += pile[take - 1];
                for (int j = take; j <= k; j++)
                    ndp[j] = Math.Max(ndp[j], dp[j - take] + sum);
            }
            dp = ndp;
        }
        return dp[k];
    }
}
