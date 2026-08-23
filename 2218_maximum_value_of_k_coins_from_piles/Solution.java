// LeetCode 2218 - Maximum Value of K Coins From Piles
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

import java.util.List;

class Solution {
    public int maxValueOfCoins(List<List<Integer>> piles, int k) {
        int[] dp = new int[k + 1];
        for (List<Integer> pile : piles) {
            int[] ndp = dp.clone();
            int sum = 0;
            for (int take = 1; take <= pile.size() && take <= k; take++) {
                sum += pile.get(take - 1);
                for (int j = take; j <= k; j++)
                    ndp[j] = Math.max(ndp[j], dp[j - take] + sum);
            }
            dp = ndp;
        }
        return dp[k];
    }
}
